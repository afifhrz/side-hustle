from pyomo.environ import *

# Create a ConcreteModel object
model = ConcreteModel()

# Define decision variables
model.x = Var(within=NonNegativeReals)
model.y = Var(within=NonNegativeReals)

# Define objective function
model.obj = Objective(expr=2 * model.x + 3 * model.y, sense=maximize)

# Define constraints
model.constraint1 = Constraint(expr=2 * model.x + model.y <= 20)
model.constraint2 = Constraint(expr=4 * model.x - 5 * model.y >= -10)
model.constraint3 = Constraint(expr=model.x + 2 * model.y <= 15)

# Solve the problem
solver = SolverFactory('gurobi')  # Replace 'glpk' with the name of your solver
results = solver.solve(model)

# Print the results
print(f"Objective value: {model.obj()}")
print(f"x = {model.x()}")
print(f"y = {model.y()}")
