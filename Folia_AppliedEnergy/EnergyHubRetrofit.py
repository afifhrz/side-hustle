# -*- coding: utf-8 -*-
"""
Single energy hub - single stage model for the optimal design of a multi-energy system including building retrofit options
Author: Georgios Mavromatidis (ETH Zurich, gmavroma@ethz.ch)
"""

import pyomo
import pyomo.opt
import pyomo.environ as pe

# import pandas as pd
import numpy as np


class EnergyHubRetrofit:
    """This class implements a standard energy hub model for the optimal design and operation of distributed multi-energy systems"""

    def __init__(self, eh_input_dict, temp_res=1, optim_mode=3, num_of_pareto_points=5):
        """
        __init__ function to read in the input data and begin the model creation process

        Inputs to the function:
        -----------------------
            * eh_input_dict: dictionary that holds all the values for the model parameters
            * temp_res (default = 1): 1: typical days optimization, 2: full horizon optimization (8760 hours), 3: typical days with continuous storage state-of-charge
            * optim_mode (default = 3): 1: for cost minimization, 2: for carbon minimization, 3: for multi-objective optimization
            * num_of_pareto_points (default = 5): In case optim_mode is set to 3, then this specifies the number of Pareto points
        """

        self.inp = eh_input_dict
        self.temp_res = temp_res
        self.optim_mode = optim_mode
        if self.optim_mode == 1 or self.optim_mode == 2:
            self.num_of_pfp = 0
            print(
                "Warning: Number of Pareto front points specified is ignored. Single-objective optimization will be performed."
            )
        else:
            self.num_of_pfp = num_of_pareto_points

    def create_model(self):
        """Create the Pyomo energy hub model given the input data specified in the self.InputFile"""

        self.m = pe.ConcreteModel()

        # %% Model sets
        # ==========

        # Temporal dimensions
        # -------------------
        self.m.Days = pe.Set(
            initialize=self.inp["Days"],
            ordered=True,
            doc="The number of days considered in each year of the model | Index: d",
        )
        self.m.Time_steps = pe.Set(
            initialize=self.inp["Time_steps"],
            ordered=True,
            doc="Time steps considered in the model | Index: t",
        )
        self.m.Investment_stages = pe.Set(
            initialize=self.inp["Investment_stages"],
            ordered=True,
            doc="Investment stages | Index: w",
        )
        self.m.Energy_system_location = pe.Set(
            initialize=self.inp["Energy_system_location"],
            ordered=False,
            doc="Energy_system_location | Index: l",
        )
        self.m.Calendar_days = pe.Set(
            initialize=list(range(1, 365 + 1)),
            ordered=True,
            doc="Set for each calendar day of a full year | Index: y",
        )
        # Energy carriers
        # ---------------
        self.m.Energy_carriers = pe.Set(
            initialize=self.inp["Energy_carriers"],
            doc="The set of all energy carriers considered in the model | Index : ec",
        )
        self.m.Energy_carriers_imp = pe.Set(
            initialize=self.inp["Energy_carriers_imp"],
            within=self.m.Energy_carriers,
            doc="The set of energy carriers for which imports are possible | Index : ec_imp",
        )
        self.m.Energy_carriers_exp = pe.Set(
            initialize=self.inp["Energy_carriers_exp"],
            within=self.m.Energy_carriers,
            doc="The set of energy carriers for which exports are possible | Index : ec_exp",
        )
        self.m.Energy_carriers_exc = pe.Set(
            initialize=self.inp["Energy_carriers_exc"],
            within=self.m.Energy_carriers,
            doc="The set of energy carriers that can be exchanged between energy system location | Index : ecx",
        )
        self.m.Energy_carriers_dem = pe.Set(
            initialize=self.inp["Energy_carriers_dem"],
            within=self.m.Energy_carriers,
            doc="The set of energy carriers for which end-user demands are defined | Index : ec_dem",
        )

        # Technologies
        # ------------
        self.m.Conversion_tech = pe.Set(
            initialize=self.inp["Conversion_tech"],
            doc="The energy conversion technologies of each energy hub candidate site | Index : conv_tech",
        )
        self.m.Solar_tech = pe.Set(
            initialize=self.inp["Solar_tech"],
            within=self.m.Conversion_tech,
            doc="Subset for solar technologies | Index : sol",
        )
        self.m.Dispatchable_tech = pe.Set(
            initialize=self.inp["Dispatchable_tech"],
            within=self.m.Conversion_tech,
            doc="Subset for dispatchable/controllable technologies | Index : disp",
        )
        self.m.Storage_tech = pe.Set(
            initialize=self.inp["Storage_tech"],
            doc="The set of energy storage technologies for each energy hub candidate site | Index : stor_tech",
        )

        # %% Model parameters
        # ================

        # Load parameters
        # ---------------
        self.m.Demands = pe.Param(
            self.m.Energy_carriers_dem,
            self.m.Energy_system_location,
            self.m.Days,
            self.m.Time_steps,
            default=0,
            initialize=self.inp["Demands"],
            doc="Time-varying energy demand patterns for the energy hub",
        )
        if self.temp_res == 1 or self.temp_res == 3:
            self.m.Number_of_days = pe.Param(
                self.m.Days,
                default=1,
                initialize=self.inp["Number_of_days"],
                doc="The number of days that each time step of typical day corresponds to",
            )
        else:
            self.m.Number_of_days = pe.Param(
                self.m.Days,
                default=1,
                initialize=1,
                doc="Parameter equal to 1 for each time step, because full horizon optimization is performed (temp_res == 2)",
            )
        if self.temp_res == 3:
            self.m.C_to_T = pe.Param(
                self.m.Calendar_days,
                initialize=self.inp["C_to_T"],
                within=self.m.Days,
                doc="Parameter to match each calendar day of a full year to a typical day for optimization",
            )

        # Technical parameters
        # --------------------
        # Energy conversion technologies
        self.m.Conv_factor = pe.Param(
            self.m.Conversion_tech,
            self.m.Energy_carriers,
            self.m.Investment_stages,
            default=0,
            initialize=self.inp["Conv_factor"],
            doc="The conversion factors of the technologies c and energy carrier ec installed in stage w",
        )
        '''input not found'''
        # self.m.Total_degradation_coefficient = pe.Param(
        #     self.m.Conversion_tech,
        #     self.m.Energy_carriers,
        #     self.m.Investment_stages,
        #     self.m.Calendar_days,
        #     default=0,
        #     initialize=self.inp["Total_degradation_coefficient"],
        #     doc="Total deg coeff for the conv factor technology c and energy carrier ec depending on w and the y",
        # )
        # self.m.Yearly_degradation_coefficient = pe.Param(
        #     self.m.Conversion_tech,
        #     self.m.Energy_carriers,
        #     default=0,
        #     initialize=self.inp["Yearly_degradation_coefficient"],
        #     doc="Yearly degradation coefficient for the conversion factor technology c and energy carrier ec",
        # )
        
        self.m.Lifetime_tech = pe.Param(
            self.m.Conversion_tech,
            initialize=self.inp["Lifetime_tech"],
            doc="Lifetime of energy generation technologies",
        )

        # sub lifetime_tech clcd (dispatchable) and clcs (solar)
        '''input not found'''
        # self.m.Lifetime_tech_clcd = pe.Param(
        #     within=self.m.Lifetime_tech,
        #     initialize=self.inp["Lifetime_tech_clcd"],
        #     doc="Lifetime of dispatchable energy generation technologies clcd",
        # )

        # self.m.Lifetime_tech_clcs = pe.Param(
        #     within=self.m.Lifetime_tech,
        #     initialize=self.inp["Lifetime_tech_clcs"],
        #     doc="Lifetime of solar energy generation technologies clcs",
        # )


        # Energy storage technologies
        self.m.Storage_tech_coupling = pe.Param(
            self.m.Storage_tech,
            self.m.Energy_carriers,
            initialize=self.inp["Storage_tech_coupling"],
            default=0,
            doc="Storage technology coupling parameters describing the energy carrier ec stored in storage technology s",
        )
        self.m.Storage_charging_eff = pe.Param(
            self.m.Storage_tech,
            initialize=self.inp["Storage_charging_eff"],
            doc="Charging efficiency of storage technology s",
        )
        self.m.Storage_discharging_eff = pe.Param(
            self.m.Storage_tech,
            initialize=self.inp["Storage_discharging_eff"],
            doc="Discharging efficiency of storage technology s",
        )
        self.m.Storage_standing_losses = pe.Param(
            self.m.Storage_tech,
            initialize=self.inp["Storage_standing_losses"],
            doc="Standing losses for the storage technologies",
        )
        self.m.Storage_max_charge = pe.Param(
            self.m.Storage_tech,
            initialize=self.inp["Storage_max_charge"],
            doc="Maximum charging rate in % of the total capacity for the storage technologies",
        )
        self.m.Storage_max_discharge = pe.Param(
            self.m.Storage_tech,
            initialize=self.inp["Storage_max_discharge"],
            doc="Maximum discharging rate in % of the total capacity for the storage technologies",
        )
        
        '''input not found'''
        # self.m.Total_degradation_coefficient_chdc = pe.Param(
        #     self.m.Storage_tech,
        #     self.m.Investment_stages,
        #     self.m.Calendar_days,
        #     initialize=self.inp["Storage_max_discharge"],
        #     doc="Total deg coeff for the charging and discharging efficiencies of s depending on the w and the y",
        # )
        # self.m.Yearly_degradation_coefficient_chdc = pe.Param(
        #     self.m.Storage_tech,
        #     initialize=self.inp["Storage_max_discharge"],
        #     doc="Yearly deg coeff for the charging and discharging efficiencies of storage technology s",
        # )
                
        self.m.Lifetime_stor = pe.Param(
            self.m.Storage_tech,
            initialize=self.inp["Lifetime_stor"],
            doc="Lifetime of energy storage technologies",
        )

        self.m.Storage_max_cap = pe.Param(
            self.m.Storage_tech,
            initialize=self.inp["Storage_max_cap"],
            doc="Maximum allowable energy storage capacity per technology type",
        )

        # Energy network
        '''input not found'''
        # self.m.Network_loses_per_m = pe.Param(
        #     self.m.Energy_carriers_exc,
        #     initialize=self.inp["Network_loses_per_m"],
        #     doc="Loses per m of network connection transferring energy carrier ecx",
        # )

        # self.m.Alpha = pe.Param(
        #     initialize=self.inp["Alpha"],
        #     doc="Empirical param for the calc of the pipe diameter for thermal net connections between locs [mm/kWh]",
        # )

        # self.m.Beta = pe.Param(
        #     initialize=self.inp["Beta"],
        #     doc="Empirical param for the calc of the pipe diameter for thermal net connections between locs [mm]",
        # )

        # self.m.Gamma = pe.Param(
        #     initialize=self.inp["Gamma"],
        #     doc="Empirical param for the calc of the pipe inv cost/m for thermal net connections between locs [CHF/m/mm]",
        # )

        # self.m.Theta = pe.Param(
        #     initialize=self.inp["Theta"],
        #     doc="Empirical param for the calc of the pipe inv cost/m for thermal net connections between locs [CHF/m]",
        # )


        # Miscellaneous technical parameters
        '''input not found'''
        # self.m.Energy_demand = pe.Param(
        #     self.m.Energy_carriers_dem,
        #     self.m.Energy_system_location,
        #     self.m.Calendar_days,
        #     self.m.Days,
        #     self.m.Time_steps,
        #     initialize=self.inp["Energy_demand"],
        #     doc="Energy demand for energy carrier ec_dem at location l in year y day d and time steps t",
        # )
        # self.m.Biomass = pe.Param(
        #     self.m.Calendar_days,
        #     initialize=self.inp["Biomass"],
        #     doc="The available bioenergy in the form of biomass per unit of building floor area in year y",
        # )
        self.m.P_solar = pe.Param(
            self.m.Energy_system_location,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            initialize=self.inp["P_solar"],
            doc="Incoming solar radiation patterns(kWh/m2) at location l in year y day d time steps t for solar techno",
        )
        # self.m.Floor_area = pe.Param(
        #     self.m.Calendar_days,
        #     initialize=self.inp["Floor_area"],
        #     doc="Total building floor area across all energy system location in year y",
        # )
        self.m.Roof_area = pe.Param(
            self.m.Energy_system_location,
            self.m.Calendar_days,
            initialize=self.inp["Roof_area"],
            doc="Total building roof area across at location l in year y for the installation of solar technologies",
        )
        # self.m.Distance_area = pe.Param(
        #     self.m.Energy_system_location,
        #     initialize=self.inp["Distance_area"],
        #     doc="Distance between energy system location l and l'",
        # )
        # self.m.Amount_calendar_days = pe.Param(
        #     self.m.Calendar_days,
        #     self.m.Days,
        #     initialize=self.inp["Amount_of_calendar_days"],
        #     doc="Number of calendar days represented by each representative day d in year y",
        # )

        # Economic parameters
        # ---------------
        self.m.Import_prices = pe.Param(
            self.m.Energy_carriers_imp,
            self.m.Calendar_days,
            initialize=self.inp["Import_prices"],
            default=0,
            doc="Prices for importing energy carriers eec_imp in year y from the grid",
        )
        self.m.Export_prices = pe.Param(
            self.m.Energy_carriers_exp,
            self.m.Calendar_days,
            initialize=self.inp["Export_prices"],
            default=0,
            doc="Feed-in tariffs for exporting energy carriers ec_exp in year y back to the grid",
        )
        self.m.Fixed_conv_costs = pe.Param(
            self.m.Conversion_tech,
            self.m.Investment_stages,
            initialize=self.inp["Fixed_conv_costs"],
            doc="Fixed cost for installation of conv technology c in investment stage w",
        )
        self.m.Linear_conv_costs = pe.Param(
            self.m.Conversion_tech,
            self.m.Investment_stages,
            initialize=self.inp["Linear_conv_costs"],
            doc="Linear capacity dependent cost for the installation of conv tech c in investment stage w",
        )
        self.m.Fixed_stor_costs = pe.Param(
            self.m.Storage_tech,
            self.m.Investment_stages,
            initialize=self.inp["Fixed_stor_costs"],
            doc="Fixed cost for the installation of storage technology s in investment stag w",
        )
        self.m.Linear_stor_costs = pe.Param(
            self.m.Storage_tech,
            self.m.Investment_stages,
            initialize=self.inp["Linear_stor_costs"],
            doc="Linear capacity dependent cost for the installation of storage technology s in investment stage w",
        )
        # self.m.Omc_cost = pe.Param(
        #     self.m.Conversion_tech,
        #     initialize=self.inp["Omc_cost"],
        #     doc="Par used to calculate annual maintenance cost for conv techno c as a fraction of its total inv cost",
        # )
        # self.m.Oms_cost = pe.Param(
        #     self.m.Storage_tech,
        #     initialize=self.inp["Oms_cost"],
        #     doc="Par used to calculate annual maintenance cost for storage techno s as a fraction of its total inv cost",
        # )
        # self.m.Salvage_conversion = pe.Param(
        #     self.m.Conversion_tech,
        #     self.m.Investment_stages,
        #     initialize=self.inp["Salvage_conversion"],
        #     doc="Salvage % of initial inv cost for conv tech c that was installed in stage w and hasn't reached the end of its lifetime",
        # )
        # self.m.Salvage_storage = pe.Param(
        #     self.m.Conversion_tech,
        #     self.m.Investment_stages,
        #     initialize=self.inp["Salvage_storage"],
        #     doc="Salvage % of initial inv cost for stor tech s that was installed in stage w and hasn't reached the end of its lifetime",
        # )
        self.m.Discount_rate = pe.Param(
            initialize=self.inp["Discount_rate"],
            doc="The interest rate used for the CRF calculation",
        )

        self.m.Network_inv_cost_per_m = pe.Param(
            initialize=self.inp["Network_inv_cost_per_m"],
            doc="Investment cost per pipe m of the thermal network of the energy hub",
        )

        # Environmental parameters
        # ------------------------
        self.m.Carbon_factors_import = pe.Param(
            self.m.Energy_carriers_imp,
            self.m.Calendar_days,
            initialize=self.inp["Carbon_factors_import"],
            doc="Carbon emission factor for imported energy carrier ec_imp in year y",
        )
        self.m.epsilon = pe.Param(
            initialize=10 ** 8,
            mutable=True,
            doc="Epsilon value used for the multi-objective epsilon-constrained optimization",
        )

        # Misc parameters
        # ---------------

        self.m.BigM = pe.Param(default=10 ** 6, doc="Big M: Sufficiently large value")

        # Parameters definitions
        # ------------------------------

        # def Total_degradation_coefficient_rule(m, conv_tech, ec):
        #     if (m.Calendar_days >= m.Investment_stages
        #     ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_tech - 1):
        #         return (1 - m.Yearly_degradation_coefficient[conv_tech, ec] ** (m.Calendar_days - m.Investment_stages)
        #                 )

        # self.m.Total_degradation_coefficient = pe.Param(
        #     self.m.Conversion_tech,
        #     self.m.Energy_carriers,
        #     self.m.Investment_stages,
        #     self.m.Calendar_days,
        #     rule=Total_degradation_coefficient_rule,
        #     doc="Total degradation coefficient cdeg rule",
        # )

        # def Total_degradation_coefficient_chdc_rule(m, stor_tech):
        #     if (m.Calendar_days >= m.Investment_stages
        #     ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_stor - 1):
        #         return (1 - m.Yearly_degradation_coefficient_chdc[stor_tech] ** (m.Calendar_days - m.Investment_stages)
        #                 )

        # self.m.Total_degradation_coefficient_chdc = pe.Param(
        #     self.m.Storage_tech,
        #     self.m.Investment_stages,
        #     self.m.Calendar_days,
        #     rule=Total_degradation_coefficient_chdc_rule,
        #     doc="Total degradation coefficient sdeg rule",
        # )

        # def Salvage_conversion_rule(m, conv_tech):
        #     if m.Investment_stages >= max(m.Calendar_days) + 1 - m.Lifetime_tech:
        #         return (1 - (1 + m.Discount_rate) ** (max(m.Calendar_days) + 1 - m.Investment_stages - m.Lifetime_tech
        #                                               ) / 1 - (1 + m.Discount_rate) ** m.Lifetime_tech[conv_tech]
        #                 )

        # self.m.Salvage_conversion = pe.Param(
        #     self.m.Conversion_tech,
        #     self.m.Investment_stages,
        #     rule=Salvage_conversion_rule,
        #     doc="Salvage conversion cslvg rule",
        # )

        # def Salvage_storage_rule(m, stor_tech):
        #     if m.Investment_stages >= max(m.Calendar_days) + 1 - m.Lifetime_stor:
        #         return (1 - (1 + m.Discount_rate) ** (max(m.Calendar_days) + 1 - m.Investment_stages - m.Lifetime_stor
        #                                               ) / 1 - (1 + m.Discount_rate) ** m.Lifetime_stor[stor_tech]
        #                 )

        # self.m.Salvage_storage = pe.Param(
        #     self.m.Storage_tech,
        #     self.m.Investment_stages,
        #     rule=Salvage_storage_rule,
        #     doc="Salvage storage sslvg rule",
        # )

        # %% Model variables
        # ===============

        # Generation technologies
        # -----------------------
        self.m.P_conv = pe.Var(
            self.m.Conversion_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            within=pe.NonNegativeReals,
            doc="Input energy to conv tech c at energy loc l, in inv stage w operating in year y, day d and time step t",
        )
        self.m.P_import = pe.Var(
            self.m.Energy_carriers_imp,
            self.m.Energy_system_location,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            within=pe.NonNegativeReals,
            doc="Imported energy carrier ec_imp at energy loc l, in year y, day d and time step t",
        )
        self.m.P_export = pe.Var(
            self.m.Energy_carriers_exp,
            self.m.Energy_system_location,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            within=pe.NonNegativeReals,
            doc="Exported energy carrier ec_exp at energy loc l, in year y, day d and time step t",
        )
        self.m.P_exchange = pe.Var(
            self.m.Energy_carriers_exc,
            self.m.Energy_system_location,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            within=pe.NonNegativeReals,
            doc="Exchanged of energy carrier exc from location l to loc l', in year y, day d, and time step t",
        )
        self.m.Conv_cap = pe.Var(
            self.m.Conversion_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            within=pe.NonNegativeReals,
            doc="Installed new capacity of conv tech c at loc l in investment stage w",
        )
        self.m.y_conv = pe.Var(
            self.m.Conversion_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            within=pe.Binary,
            doc="Binary variable denoting the installation (=1) of energy conversion tech c at loc l in inv stage w",
        )

        # Storage technologies
        # -------------------
        self.m.Qin = pe.Var(
            self.m.Storage_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            within=pe.NonNegativeReals,
            doc="Charging energy for storage tech s at en loc l, in inv stage w, operating year y, day d & time steps t",
        )
        self.m.Qout = pe.Var(
            self.m.Storage_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            within=pe.NonNegativeReals,
            doc="Discharging energy for stor tech s at en loc l, in inv stage w, operating year y, day d & time steps t",
        )
        if self.temp_res != 3:
            self.m.SoC = pe.Var(
                self.m.Storage_tech,
                self.m.Days,
                self.m.Time_steps,
                within=pe.NonNegativeReals,
                doc="Storage state of charge",
            )
        else:
            self.m.SoC = pe.Var(
                self.m.Storage_tech,
                self.m.Calendar_days,
                self.m.Time_steps,
                within=pe.NonNegativeReals,
                doc="Storage state of charge",
            )
        self.m.Storage_cap = pe.Var(
            self.m.Storage_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            within=pe.NonNegativeReals,
            doc="Installed new capacity of storage tech s at loc l in investment stage w",
        )
        self.m.y_stor = pe.Var(
            self.m.Storage_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            within=pe.Binary,
            doc="Binary variable denoting the installation (=1) of energy storage technology at loc l in inv stage w",
        )

        # Network system design
        # ------------------
        self.m.dm = pe.Var(
            self.m.Energy_system_location,
            within=pe.NonNegativeReals,
            doc="Pipe diameter for thermal connections between energy system loc l, l2",
        )

        self.m.LC = pe.Var(
            self.m.Energy_system_location,
            within=pe.NonNegativeReals,
            doc="Interconnection cost to exchange energy carrier ecx between l and l2",
        )

        self.m.y_net = pe.Var(
            self.m.Energy_carriers_exc,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            within=pe.Binary,
            doc="Binary var denoting the initial connection to exchange energy carrier ecx between loc in inv stg w",
        )


        # Objective function components
        # -----------------------------
        self.m.Total_cost = pe.Var(
            within=pe.NonNegativeReals,
            doc="Total cost for the investment and the operation of the energy hub",
        )
        self.m.Total_carbon = pe.Var(
            within=pe.NonNegativeReals,
            doc="Total carbon emissions due to the operation of the energy hub",
        )
        self.m.Import_cost = pe.Var(
            self.m.Energy_system_location,
            self.m.Calendar_days,
            within=pe.NonNegativeReals,
            doc="Total cost due to energy carrier imports at loc l in year y",
        )
        self.m.Maintenance_cost = pe.Var(
            self.m.Energy_system_location,
            self.m.Calendar_days,
            within=pe.NonNegativeReals,
            doc="Total maint cost for all conv and stor tech installed at loc l in year y",
        )
        self.m.Export_profit = pe.Var(
            self.m.Energy_system_location,
            self.m.Calendar_days,
            within=pe.NonNegativeReals,
            doc="Total income due to exported electricity at loc l in year y",
        )
        self.m.Salvage_value = pe.Var(
            self.m.Energy_system_location,
            within=pe.NonNegativeReals,
            doc="Salvage value of all conv and storage tech at location l not reaching the end of their lifetime",
        )
        self.m.Investment_cost = pe.Var(
            within=pe.NonNegativeReals,
            doc="Investment cost of all energy technologies in the energy hub",
        )

        # %% Model constraints
        # =================

        # Energy demand balances
        # ----------------------
        def Load_balance_rule(m, ec, ecx, ec_exp, ec_dem, l, l2, w, y, d, t):
            return (m.P_import[ec, l, y, d, t] if ec in m.Energy_carriers_imp else 0) + sum(
                m.P_conv[conv_tech, l, w, y, d, t] * m.Conv_factor[conv_tech, ec, w, y]
                * m.Total_degradation_coefficient[conv_tech, ec, w, y]
                for conv_tech in m.Conversion_tech
            ) + sum(
                m.Storage_tech_coupling[stor_tech, ec]
                * (m.Qout[stor_tech, l, w, y, d, t] - m.Qin[stor_tech, l, w, y, d, t])
                for stor_tech in m.Storage_tech
            ) + sum(
                m.P_exchange[ec, l2, l, y, d, t]
                * (1 - (m.Network_loses_per_m[ec] * m.Distance_area[l2, l]))
                - m.P_exchange[ecx, l, y, d, t]) - m.P_export[ec_exp, l, l2, y, d, t] == (
                       m.Demands[ec_dem, l, y, d, t]
                   )

        self.m.Load_balance = pe.Constraint(
            self.m.Energy_carriers,
            self.m.Energy_system_location,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            rule=Load_balance_rule,
            doc="Energy balance for the energy hub including conversion, storage, losses, exchange and export flows",
        )

        # Generation constraints
        # ----------------------
        def Capacity_constraint_rule(m, disp, ec, l, y, d, t, w):
            if (m.Calendar_days >= m.Investment_stages
            ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_tech - 1
            ) and (m.Conv_factor[disp, ec, w]) > 0:
                return (
                        m.P_conv[disp, l, w, y, d, t] * m.Conv_factor[disp, ec, w]
                        * m.Total_degradation_coefficient[disp, ec, w, y] <= m.Conv_cap[disp, l, w]
                )
            else:
                return pe.Constraint.Skip

        self.m.Capacity_constraint = pe.Constraint(
            self.m.Dispatchable_tech,
            self.m.Energy_carriers,
            self.m.Energy_system_location,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            self.m.Investment_stages,
            self.m.Lifetime_tech,
            self.m.Conv_factor,
            rule=Capacity_constraint_rule,
            doc="Constraint preventing capacity violation for the generation technologies of the energy hub",
        )

        def Solar_input_rule(m, stor_tech, l, w, y, d, t):
            if (m.Calendar_days >= m.Investment_stages
            ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_tech - 1):
                return (m.P_conv[stor_tech, l, w, y, d, t] == m.P_solar[l, y, d, t] * m.Conv_cap[stor_tech, l, w]
                        )

        self.m.Solar_input = pe.Constraint(
            self.m.Solar_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            rule=Solar_input_rule,
            doc="Constraint connecting the solar radiation per m2 with the area of solar PV technologies",
        )

        def Roof_area_non_violation_rule(m, l, y, w):
            return sum(m.Conv_cap[sol, l, w] for sol in m.Solar_tech) <= m.Roof_area[l, y]

        self.m.Roof_area_non_violation = pe.Constraint(
            rule=Roof_area_non_violation_rule,
            doc="Non violation of the maximum roof area for solar installations",
        )

        def Annual_consumption_of_biomass_rule(m, ec, l, y, d, t):
            return sum(m.P_import[ec, l, d, t] * m.Amount_calendar_days[y, d]) <= (m.Biomass[y] * m.Floor_area[y])

        self.m.Annual_consumption_of_biomass_rule = pe.Constraint(
            rule=Annual_consumption_of_biomass_rule,
            doc="limits the total annual consumption of biomass across all sites to account for biomass availability",
        )

        def Big_M_constraint_conversion(m, conversion_tech, l, w):
            return m.Conv_cap[conversion_tech, l, w] <= (m.BigM * m.y_conv[conversion_tech, l, w])

        self.m.Big_M_constraint_conversion = pe.Constraint(
            self.m.Conversion_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            rule=Big_M_constraint_conversion,
            doc="Big-M const that forces binary variable 𝑌 to be equal to 1, if the variable 𝑁𝐶𝐴𝑃 gets a non-0 value",
        )

        def Minimum_part_load_constr_rule1(m, disp, ec, d, t):
            return (
                    m.P_conv[disp, d, t] * m.Conv_factor[disp, ec]
                    <= m.BigM * m.y_on[disp, d, t]
            )

        def Minimum_part_load_constr_rule2(m, disp, ec, d, t):
            return (
                    m.P_conv[disp, d, t] * m.Conv_factor[disp, ec]
                    + m.BigM * (1 - m.y_on[disp, d, t])
                    >= m.Minimum_part_load[disp] * m.Conv_cap[disp]
            )

        self.m.Mininum_part_rule_constr1 = pe.Constraint(
            (
                (disp, ec, d, t)
                for disp in self.m.Dispatchable_tech
                for ec in self.m.Energy_carriers
                for d in self.m.Days
                for t in self.m.Time_steps
                if self.m.Conv_factor[disp, ec] > 0
            ),
            rule=Minimum_part_load_constr_rule1,
            doc="Constraint enforcing a minimum load during the operation of a dispatchable energy technology",
        )

        self.m.Mininum_part_rule_constr2 = pe.Constraint(
            (
                (disp, ec, d, t)
                for disp in self.m.Dispatchable_tech
                for ec in self.m.Energy_carriers
                for d in self.m.Days
                for t in self.m.Time_steps
                if self.m.Conv_factor[disp, ec] > 0
            ),
            rule=Minimum_part_load_constr_rule2,
            doc="Constraint enforcing a minimum load during the operation of a dispatchable energy technology",
        )

        def Fixed_cost_constr_rule(m, conv_tech):
            return m.Conv_cap[conv_tech] <= m.BigM * m.y_conv[conv_tech]

        self.m.Fixed_cost_constr = pe.Constraint(
            self.m.Conversion_tech,
            rule=Fixed_cost_constr_rule,
            doc="Constraint for the formulation of the fixed cost in the objective function",
        )

        # Storage constraints
        # -------------------
        # -------------------
        def Storage_balance_rule(m, stor_tech, l, w, y, d, t):
            if self.temp_res == 1:
                if (m.Calendar_days >= m.Investment_stages
                ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_stor - 1) and (t != 1):
                    return (
                            m.SoC[stor_tech, l, w, y, d, t]
                            == (1 - m.Storage_standing_losses[stor_tech])
                            * m.SoC[stor_tech, l, w, y, d, t - 1]
                            + (m.Storage_charging_eff[stor_tech] * m.Qin[stor_tech, l, w, y, d, t]
                               * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                            - (1 / m.Storage_discharging_eff[stor_tech]
                               * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                            * m.Qout[stor_tech, d, t]
                    )
                else:
                    return (
                            m.SoC[stor_tech, l, w, y, d, t]
                            == (1 - m.Storage_standing_losses[stor_tech])
                            * m.SoC[stor_tech, l, w, d, t + max(m.Time_steps) - 1]
                            + (m.Storage_charging_eff[stor_tech] * m.Qin[stor_tech, l, w, y, d, t]
                                * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                            - (1 / m.Storage_discharging_eff[stor_tech]
                                * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                            * m.Qout[stor_tech, d, t]
                    )

            elif self.temp_res == 2:
                if (m.Calendar_days >= m.Investment_stages
                ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_stor - 1) and (t != 1):
                    return (
                            m.SoC[stor_tech, l, w, y, d, t]
                            == (1 - m.Storage_standing_losses[stor_tech])
                            * m.SoC[stor_tech, l, w, y, d, t - 1]
                            + (m.Storage_charging_eff[stor_tech] * m.Qin[stor_tech, l, w, y, d, t]
                               * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                            - (1 / m.Storage_discharging_eff[stor_tech]
                               * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                            * m.Qout[stor_tech, d, t]
                    )
                else:
                    if d != 1:
                        return (
                                m.SoC[stor_tech, l, w, y, d, t]
                                == (1 - m.Storage_standing_losses[stor_tech])
                                * m.SoC[stor_tech, l, w, d - 1, t + max(m.Time_steps) - 1]
                                + (m.Storage_charging_eff[stor_tech] * m.Qin[stor_tech, l, w, y, d, t]
                                   * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                                - (1 / m.Storage_discharging_eff[stor_tech]
                                   * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                                * m.Qout[stor_tech, d, t]
                        )
                    else:
                        return (
                                m.SoC[stor_tech, l, w, y, d, t]
                                == (1 - m.Storage_standing_losses[stor_tech])
                                * m.SoC[stor_tech, l, w, d + 364, t + max(m.Time_steps) - 1]
                                + (m.Storage_charging_eff[stor_tech] * m.Qin[stor_tech, l, w, y, d, t]
                                   * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                                - (1 / m.Storage_discharging_eff[stor_tech]
                                   * m.Total_degradation_coefficient_chdc[stor_tech, w, y])
                                * m.Qout[stor_tech, d, t]
                        )

            elif self.temp_res == 3:
                if (m.Calendar_days >= m.Investment_stages
                ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_stor - 1) and (t != 1):
                    return (
                            m.SoC[stor_tech, l, w, y, d, t]
                            == (1 - m.Storage_standing_losses[stor_tech])
                            * m.SoC[stor_tech, l, w, d, t - 1]
                            + m.Storage_charging_eff[stor_tech] * m.Total_degradation_coefficient_chdc[stor_tech, w, y]
                            * sum(m.Qin[stor_tech, m.C_to_T[d], t]
                    )
                            - (1 / m.Storage_discharging_eff[stor_tech])
                            * m.Total_degradation_coefficient_chdc[stor_tech, w, y]
                            * sum(m.Qout[stor_tech, m.C_to_T[d], t]
                    )
                    )
                else:
                    if (m.Calendar_days >= m.Investment_stages
                ) and (m.Calendar_days <= m.Investment_stages + m.Lifetime_stor - 1) and (d != 1):
                        return (
                                m.SoC[stor_tech, l, w, y, d, t]
                                == (1 - m.Storage_standing_losses[stor_tech])
                                * m.SoC[stor_tech, l, w, d - 1, t + max(m.Time_steps) - 1]
                                + m.Storage_charging_eff[stor_tech] * m.Total_degradation_coefficient_chdc[stor_tech, w, y]
                                * sum(m.Qin[stor_tech, m.C_to_T[d], t]
                        )
                                - (1 / m.Storage_discharging_eff[stor_tech])
                                * m.Total_degradation_coefficient_chdc[stor_tech, w, y]
                                * sum(m.Qout[stor_tech, m.C_to_T[d], t]
                        )
                        )
                    else:
                        return (
                                m.SoC[stor_tech, l, w, y, d, t]
                                == (1 - m.Storage_standing_losses[stor_tech])
                                * m.SoC[stor_tech, d + max(m.Calendar_days) - 1, t + max(m.Time_steps) - 1]
                                + m.Storage_charging_eff[stor_tech] * m.Total_degradation_coefficient_chdc[stor_tech, w, y]
                                * sum(m.Qin[stor_tech, m.C_to_T[d], t]
                        )
                                - (1 / m.Storage_discharging_eff[stor_tech])
                                * sum(m.Qout[stor_tech, m.C_to_T[d], t]
                        )
                        )

        if self.temp_res == 1 or self.temp_res == 2:
            self.m.Storage_balance = pe.Constraint(
                self.m.Storage_tech,
                self.m.Days,
                self.m.Time_steps,
                rule=Storage_balance_rule,
                doc="Energy balance for the storage modules considering incoming and outgoing energy flows",
            )
        elif self.temp_res == 3:
            self.m.Storage_balance = pe.Constraint(
                self.m.Storage_tech,
                self.m.Calendar_days,
                self.m.Time_steps,
                rule=Storage_balance_rule,
                doc="Energy balance for the storage modules considering incoming and outgoing energy flows",
            )

        def Storage_charg_rate_constr_rule(m, stor_tech, l, w, y, d, t):
            return (
                    m.Qin[stor_tech, l, w, y, d, t]
                    <= m.Storage_max_charge[stor_tech, l, w, y, d, t] * m.Storage_cap[stor_tech, l, w]
            )

        self.m.Storage_charg_rate_constr = pe.Constraint(
            self.m.Storage_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            rule=Storage_charg_rate_constr_rule,
            doc="Constraint for the maximum allowable charging rate of the storage technologies",
        )

        def Storage_discharg_rate_constr_rule(m, stor_tech, l, w, y, d, t):
            return (
                    m.Qout[stor_tech, l, w, y, d, t]
                    <= m.Storage_max_charge[stor_tech, l, w, y, d, t] * m.Storage_cap[stor_tech, l, w]
            )

        self.m.Storage_discharg_rate_constr = pe.Constraint(
            self.m.Storage_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            rule=Storage_discharg_rate_constr_rule,
            doc="Constraint for the maximum allowable discharging rate of the storage technologies",
        )

        def Storage_cap_constr_rule(m, stor_tech, l, w, y, d, t):
            if (m.Calendar_days >= m.Investment_stages) and (
                    m.Calendar_days <= m.Investment_stages + m.Conversion_tech - 1):
                return (m.SoC[stor_tech, l, w, y, d, t] <= m.Storage_cap[stor_tech, l, w]
                        )

        if self.temp_res == 1 or self.temp_res == 2:
            self.m.Storage_cap_constr = pe.Constraint(
                self.m.Storage_tech,
                self.m.Energy_system_location,
                self.m.Investment_stages,
                self.m.Days,
                self.m.Time_steps,
                rule=Storage_cap_constr_rule,
                doc="Constraint for non-violation of the capacity of the storage",
            )
        elif self.temp_res == 3:
            self.m.Storage_cap_constr = pe.Constraint(
                self.m.Storage_tech,
                self.m.Energy_system_location,
                self.m.Investment_stages,
                self.m.Calendar_days,
                self.m.Time_steps,
                rule=Storage_cap_constr_rule,
                doc="Constraint for non-violation of the capacity of the storage",
            )

        def Big_M_constraint_storage(m, stor_tech, l, w):
            return (m.Storage_cap[stor_tech, l, w]) <= (m.BigM * m.y_stor[stor_tech, l, w])

        self.m.Big_M_constraint_storage = pe.Constraint(
            self.m.Storage_tech,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            rule=Big_M_constraint_storage,
            doc="Big-M const that forces binary variable 𝑌 to be equal to 1, if the variable 𝑁𝐶𝐴𝑃 gets a non-0 value",
        )

        def Max_allowable_storage_cap_rule(m, stor_tech):
            return m.Storage_cap[stor_tech] <= m.Storage_max_cap[stor_tech]

        self.m.Max_allowable_storage_cap = pe.Constraint(
            self.m.Storage_tech,
            rule=Max_allowable_storage_cap_rule,
            doc="Constraint enforcing the maximum allowable storage capacity per type of storage technology",
        )

        def Fixed_cost_storage_rule(m, stor_tech):
            return m.Storage_cap[stor_tech] <= m.BigM * m.y_stor[stor_tech]

        self.m.Fixed_cost_storage = pe.Constraint(
            self.m.Storage_tech,
            rule=Fixed_cost_storage_rule,
            doc="Constraint for the formulation of the fixed cost in the objective function",
        )

        # Network constraints
        # -------------------

        def Network_connection_rule(m, ecx, l, w):
            return sum(m.y_net[ecx, l, w]) <= 1

        self.m.Network_connection = pe.Constraint(
            self.m.Energy_carriers_exc,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            rule=Network_connection_rule,
            doc="Constraint for the initial connection (occur once during the project horizon)",
        )

        def Bidirectional_connection_rule(m, ecx, l, l2, w):
            return m.y_net[ecx, l, l2, w] <= m.y_net[ecx, l2, l, w]

        self.m.Bidirectional_connection_rule = pe.Constraint(
            self.m.Energy_carriers_exc,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            rule=Bidirectional_connection_rule,
            doc="Specifies that this connection is bidirectional",
        )

        def Big_M_constraint_network(m, ecx, l, l2, w, y, d, t):
            return m.P_exchange[ecx, l, l2, y, d, t] <= m.BigM * sum(m.y_net[ecx, l, l2, w])

        self.m.Big_M_constraint_network = pe.Constraint(
            self.m.Energy_carriers_exc,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            rule=Big_M_constraint_network,
            doc="Const that allows energy to be exch between 2 loc only if a connection between them already exists",
        )

        def Pipe_diameter(m, ecx, l, l2, y, d, t, w):
            return m.dm[l, l2] >= m.Alpha * m.P_exchange[ecx, l, l2, y, d, t] + m.Beta * sum(m.y_net[ecx, l, l2, w])

        self.m.Pipe_diameter = pe.Constraint(
            self.m.Energy_carriers_exc,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            self.m.Calendar_days,
            self.m.Days,
            self.m.Time_steps,
            rule=Pipe_diameter,
            doc="Const that is used to calculate pipe diameter for the thermal interconnection between two locs",
        )

        def Bidirectional_pipe_diameter(m, l, l2):
            return m.dm[l, l2] == m.dm[l2, l]

        self.m.Bidirectional_pipe_diameter = pe.Constraint(
            self.m.Energy_system_location,
            rule=Bidirectional_pipe_diameter,
            doc="Const that is used to describe pipe d for the bidirectional thermal interconnection between two locs",
        )

        def Piping_cost_per_m(m, ecx, l, l2, w):
            return m.LC[l, l2] == m.Gamma * m.dm[l, l2] + m.Theta * sum(m.y_net[ecx, l, l2, w])

        self.m.Piping_cost_per_m = pe.Constraint(
            self.m.Energy_carriers_exc,
            self.m.Energy_system_location,
            self.m.Investment_stages,
            rule=Piping_cost_per_m,
            doc="Const that is used to calculate the piping cost per m of network connection as a function of diameter",
        )

        # Objective function definitions
        # ------------------------------
        def Investment_cost_conv_stor_rule(m, l, w):
            return m.Investment_cost_conv_stor == sum(
                (
                        m.Linear_conv_costs[conv_tech, w] * m.Conv_cap[conv_tech, l, w]
                        + m.Fixed_conv_costs[conv_tech, w] * m.y_conv[conv_tech, l, w]

                )
                for conv_tech in m.Conversion_tech
            ) + sum(
                (
                        m.Linear_stor_costs[stor_tech, w] * m.Storage_cap[stor_tech, l, w]
                        + m.Fixed_stor_costs[stor_tech, w] * m.y_stor[stor_tech, l, w]
                )
                for stor_tech in m.Conversion_tech
            )

        self.m.Investment_cost_conv_stor_rule_def = pe.Constraint(
            rule=Investment_cost_conv_stor_rule,
            doc="Individual expenditures for energy conversion and storage technologies",
        )

        def Investment_cost_net_rule(m, ecx, l, w):
            return m.Investment_cost_net == sum(
                m.y_net[ecx, l, w] * m.LC[l] * m.Distance_area * 0.5)

        self.m.Investment_cost_net_rule_def = pe.Constraint(
            rule=Investment_cost_net_rule,
            doc="Expenditure for energy networks to connect individual D-MES",
        )

        def Import_cost_rule(m, l, y):
            return m.Import_cost == sum(
                m.Import_prices[ec_imp, y] * m.P_import[ec_imp, l, y, d, t] * m.Number_of_days[y, d]
                for ec_imp in m.Energy_carriers_imp
                for d in m.Days
                for t in m.Time_steps
            )

        self.m.Import_cost_def = pe.Constraint(
            rule=Import_cost_rule,
            doc="Energy carrier import cost",
        )

        def Maintenance_cost_rule(m, l, w):
            return m.Maintenance_cost == sum((
                (
                    m.Linear_conv_costs[conv_tech, w] * m.Conv_cap[conv_tech, l, w]
                    + m.Fixed_conv_costs[conv_tech, w] * m.y_conv[conv_tech, l, w]
                )
            ) * m.Omc_cost[conv_tech]
                for conv_tech in m.Conversion_tech
            ) + sum((
                (
                    m.Linear_stor_costs[stor_tech, w] * m.Storage_cap[stor_tech, l, w]
                    + m.Fixed_stor_costs[stor_tech, w] * m.y_stor[stor_tech, l, w]
                )
            ) * m.Oms_cost[stor_tech]
                for stor_tech in m.Conversion_tech
            )

        self.m.Maintenance_cost_def = pe.Constraint(
            rule=Maintenance_cost_rule,
            doc="Maintenance cost",
        )

        def Export_profit_rule(m, l, y):
            return m.Export_profit == sum(
                m.Export_prices[ec_exp, y] * m.P_export[ec_exp, l, y, d, t] * m.Number_of_days[y, d]
                for ec_exp in m.Energy_carriers_exp
                for d in m.Days
                for t in m.Time_steps
            )

        self.m.Export_profit_def = pe.Constraint(
            rule=Export_profit_rule,
            doc="Definition of the income due to electricity exports component of the total energy system cost",
        )

        def Individual_salvage_value_rule(m, l, w):
            return m.Salvage_value == sum((
                (
                    m.Linear_conv_costs[conv_tech, w] * m.Conv_cap[conv_tech, l, w]
                    + m.Fixed_conv_costs[conv_tech, w] * m.y_conv[conv_tech, l, w]

                )
            ) * m.Salvage_conversion[conv_tech]
                for conv_tech in m.Conversion_tech
            ) + sum((
                (
                    m.Linear_stor_costs[stor_tech, w] * m.Storage_cap[stor_tech, l, w]
                    + m.Fixed_stor_costs[stor_tech, w] * m.y_stor[stor_tech, l, w]
                )
            ) * m.Salvage_storage[stor_tech]
                for stor_tech in m.Conversion_tech
            )

        self.m.Individual_salvage_value_rule = pe.Constraint(
            rule=Individual_salvage_value_rule,
            doc="Individual salvage value terms",
        )

        def Investment_expenditure_rule(m):
            return m.Investment_expenditure == sum(m.Investment_cost_conv_stor + m.Investment_cost_net) * 1 / (
                    (1 + m.Discount_rate) ** m.Investment_stages
            )

        self.m.Investment_expenditure_def = pe.Constraint(
            rule=Investment_expenditure_rule,
            doc="Investment expenditures",
        )

        def Operating_expenditure_rule(m):
            return m.Operating_expenditure == sum(m.Import_cost + m.m.Maintenance_cost - m.Export_profit) * 1 / (
                    (1 + m.Discount_rate) ** m.Calendar_days
            )

        self.m.Operating_expenditure_def = pe.Constraint(
            rule=Operating_expenditure_rule,
            doc="Operating expenditures",
        )

        def Total_salvage_value_rule(m):
            return m.Total_salvage_value == sum(m.Import_cost + m.m.Maintenance_cost - m.Export_profit) * 1 / (
                    (1 + m.Discount_rate) ** (max(m.Calendar_days) + 1)
            )

        self.m.Total_salvage_value_def = pe.Constraint(
            rule=Total_salvage_value_rule,
            doc="Total salvage value",
        )

        def Total_cost_rule(m):
            return m.Total_cost == m.Investment_expenditure + m.Operating_expenditure - m.Total_salvage_value

        self.m.Total_cost_def = pe.Constraint(
            rule=Total_cost_rule,
            doc="Definition of the total cost model objective function",
        )

        def Total_carbon_rule(m, l, y):
            return m.Total_carbon == sum(
                m.Carbon_factors_import[ec_imp, y] * m.P_import[ec_imp, l, y, d, t] * m.Number_of_days[y, d]
                for ec_imp in m.Energy_carriers_imp
                for d in m.Days
                for t in m.Time_steps
            )

        self.m.Total_carbon_def = pe.Constraint(
            rule=Total_carbon_rule,
            doc="Definition of the total carbon emissions model objective function",
        )

        # %% Objective functions
        # ===================

        # Cost objective
        # --------------
        def cost_obj_rule(m):
            return m.Total_cost

        self.m.Cost_obj = pe.Objective(rule=cost_obj_rule, sense=pe.minimize)

        # Carbon objective
        # ----------------
        def carbon_obj_rule(m):
            return m.Total_carbon

        self.m.Carbon_obj = pe.Objective(rule=carbon_obj_rule, sense=pe.minimize)

    def solve(self, mip_gap=0.001, time_limit=10 ** 8, results_folder=".\\"):
        """
        Solves the model and outputs model results

        Two types of model outputs are generated:

            1. All the model definitions, constraints, parameter and variable values are given for each objective/Pareto point in the self.results object.
            2. The key objective function, design and operation results are given as follows:
                * obj: Contains the total cost, cost breakdown, and total carbon results. It is a data frame for all optim_mode settings.
                * dsgn: Contains the generation and storage capacities of all candidate technologies. It is a data frame for all optim_mode settings.
                * oper: Contains the generation, export and storage energy flows for all time steps considered. It is a single dataframe when optim_mode is 1 or 2 (single-objective) and a list of dataframes for each Pareto point when optim_mode is set to 3 (multi-objective).
        """

        import Output_functions as of
        import pickle as pkl

        # ====================================|
        # Main optimization solving procedure |
        # ====================================|

        # Solver definition
        # -----------------
        optimizer = pyomo.opt.SolverFactory("gurobi")
        optimizer.options["MIPGap"] = mip_gap
        optimizer.options["TimeLimit"] = time_limit

        if self.optim_mode == 1:

            # Cost minimization
            # =================
            all_vars = [None]

            self.m.Carbon_obj.deactivate()
            results = optimizer.solve(
                self.m, tee=True, keepfiles=True, logfile="gur.log"
            )

            # Save results
            # ------------
            self.m.solutions.store_to(results)
            all_vars[0] = of.get_all_vars(self.m)

            # JSON file with results
            results.write(
                filename=results_folder + "\cost_min_solver_results.json", format="json"
            )

            # Pickle file with all variable values
            file = open(results_folder + "\cost_min.p", "wb")
            pkl.dump(all_vars, file)
            file.close()

            # Excel file with all variable values
            of.write_all_vars_to_excel(all_vars[0], results_folder + "\cost_min")

        elif self.optim_mode == 2:

            # Carbon minimization
            # ===================
            all_vars = [None]

            self.m.Carbon_obj.activate()
            self.m.Cost_obj.deactivate()
            optimizer.solve(self.m, tee=True, keepfiles=True, logfile="gur.log")
            carb_min = pe.value(self.m.Total_system_carbon) * 1.01

            self.m.epsilon = carb_min
            self.m.Carbon_obj.deactivate()
            self.m.Cost_obj.activate()
            results = optimizer.solve(
                self.m, tee=True, keepfiles=True, logfile="gur.log"
            )

            # Save results
            # ------------
            self.m.solutions.store_to(results)
            all_vars[0] = of.get_all_vars(self.m)

            # JSON file with results
            results.write(
                filename=results_folder + "\carb_min_solver_results.json", format="json"
            )

            # Pickle file with all variable values
            file = open(results_folder + "\carb_min.p", "wb")
            pkl.dump(all_vars, file)
            file.close()

            # Excel file with all variable values
            of.write_all_vars_to_excel(all_vars[0], results_folder + "\carb_min")

        else:

            # Multi-objective optimization
            # ============================
            all_vars = [None] * (self.num_of_pfp + 2)

            # Cost minimization
            # -----------------
            self.m.Carbon_obj.deactivate()
            results = optimizer.solve(
                self.m, tee=True, keepfiles=True, logfile="gur.log"
            )
            carb_max = pe.value(self.m.Total_system_carbon)

            # Save results
            # ------------
            self.m.solutions.store_to(results)
            all_vars[0] = of.get_all_vars(self.m)

            # JSON file with results
            results.write(
                filename=results_folder + "\MO_solver_results_1.json", format="json"
            )

            # Pickle file with all variable values
            file = open(results_folder + "\multi_obj_1.p", "wb")
            pkl.dump([all_vars[0]], file)
            file.close()

            # Excel file with all variable values
            of.write_all_vars_to_excel(all_vars[0], results_folder + "\multi_obj_1")

            # Carbon minimization
            # -------------------
            self.m.Carbon_obj.activate()
            self.m.Cost_obj.deactivate()
            optimizer.solve(self.m, tee=True, keepfiles=True, logfile="gur.log")
            carb_min = pe.value(self.m.Total_system_carbon) * 1.01

            # Pareto points
            # -------------
            if self.num_of_pfp == 0:
                self.m.epsilon = carb_min
                self.m.Carbon_obj.deactivate()
                self.m.Cost_obj.activate()
                results = optimizer.solve(
                    self.m, tee=True, keepfiles=True, logfile="gur.log"
                )

                # Save results
                # ------------
                self.m.solutions.store_to(results)
                all_vars[1] = of.get_all_vars(self.m)

                # JSON file with results
                results.write(
                    filename=results_folder + "\MO_solver_results_2.json", format="json"
                )

                # Pickle file with all variable values
                file = open(results_folder + "\multi_obj_2.p", "wb")
                pkl.dump([all_vars[1]], file)
                file.close()

                # Excel file with all variable values
                of.write_all_vars_to_excel(all_vars[1], results_folder + "\multi_obj_2")

            else:
                self.m.Carbon_obj.deactivate()
                self.m.Cost_obj.activate()

                interval = (carb_max - carb_min) / (self.num_of_pfp + 1)
                steps = list(np.arange(carb_min, carb_max, interval))
                steps.reverse()
                print(steps)

                for i in range(1, self.num_of_pfp + 1 + 1):
                    self.m.epsilon = steps[i - 1]
                    print(self.m.epsilon.extract_values())
                    results = optimizer.solve(
                        self.m, tee=True, keepfiles=True, logfile="gur.log"
                    )

                    # Save results
                    # ------------
                    self.m.solutions.store_to(results)
                    all_vars[i] = of.get_all_vars(self.m)

                    # JSON file with results
                    results.write(
                        filename=results_folder
                                 + "\MO_solver_results_"
                                 + str(i + 1)
                                 + ".json",
                        format="json",
                    )

                    # Pickle file with all variable values
                    file = open(
                        results_folder + "\multi_obj_" + str(i + 1) + ".p", "wb"
                    )
                    pkl.dump([all_vars[i]], file)
                    file.close()

                    # Excel file with all variable values
                    of.write_all_vars_to_excel(
                        all_vars[i], results_folder + "\multi_obj_" + str(i + 1)
                    )

            # Pickle file with all variable values for all multi-objective runs
            file = open(results_folder + "\multi_obj_all_points.p", "wb")
            pkl.dump(all_vars, file)
            file.close()


if __name__ == "__main__":
    pass
