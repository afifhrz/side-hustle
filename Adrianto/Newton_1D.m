clear; clc;

% Setting parameter
n_grid = 20;
P_in = 5000*ones(n_grid,1); P_left = 4500; 
dp_pert = 5; tol = 1e-6; maxiter = 200;
perm = 10; por = 0.10; eta = 0.00633*perm/por;
dx = 2.5; dt = 0.0069; end_time = 0.0833; sim_time = 0:dt:6*dt;
P = zeros(length(P_in), length(sim_time));
P(:,1) = P_in; P_Left = P_left*(ones(length(sim_time)-1,1));

% Newton iteration
for t = 2:length(sim_time)
    disp("-----------------------------------------")
    disp("Time step: " + t)
    disp("Simulation time: " + sim_time(t) + "days")
    % Guess pressure = Pressure at previous iteration.
    P(:,t) = P(:,t-1);
    P_cell = P(:,t);
    [P_west, P_east] = deal(zeros(length(P_in),1));
    % Determine pressures in neighboring cells (P_west & P_east)
    for i=1:length(P_in)
        switch i
		    case 1 % most-left grid
			    P_west(i) = P_left;
			    P_east(i) = P(i+1, t);
		    case length(P_in) % most-right grid
			    P_west(i) = P(i-1, t);
			    P_east(i) = P(i, t);	
		    otherwise % inner grid
			    P_west(i) = P(i-1, t);
			    P_east(i) = P(i+1, t);
        end
    end
    % Calculate residual for each cells
    res = residual(P_west, P_cell, P_east, P(:,t-1), dx, dt,eta);
    n = 1;
    while (max(abs(res))) > tol
        disp("Iterasi ke: " + n)       
        jac = zeros(length(P_in), length(P_in));
        % Calculate Jacobian
        for i=1:length(P_in)
            jac(i,i) = (residual(P_west(i), P_cell(i)+dp_pert, P_east(i), P(i, t-1), dx, dt, eta) - res(i)) / dp_pert;
            if i == 1 % most-left grid
                jac(i,i+1) = (residual(P_west(i), P_cell(i), P_east(i)+dp_pert, P(i, t-1), dx, dt, eta) - res(i)) / dp_pert;
            elseif i == length(P_in) % most-right grid
                jac(i,i-1) = (residual(P_west(i)+dp_pert, P_cell(i), P_east(i), P(i, t-1), dx, dt, eta) - res(i)) / dp_pert;
            else % inner grid
                jac(i,i-1) = (residual(P_west(i)+dp_pert, P_cell(i), P_east(i), P(i, t-1), dx, dt, eta) - res(i)) / dp_pert;
                jac(i,i+1) = (residual(P_west(i), P_cell(i), P_east(i)+dp_pert, P(i, t-1), dx, dt, eta) - res(i)) / dp_pert;
            end
        end

        incr = -jac\res; % Calculate delta P
        P(:,t) = P(:,t) + incr; % Update guess Pressure
        P_cell = P(:,t);
        % Determine pressures in neighboring cells (P_west & P_east)
        for i=1:length(P_in)
            switch i
		        case 1 % most-left grid
			        P_west(i) = P_left;
			        P_east(i) = P(i+1, t);
		        case length(P_in) % most-right grid
			        P_west(i) = P(i-1, t);
			        P_east(i) = P(i, t);	
		        otherwise % inner grid
			        P_west(i) = P(i-1, t);
			        P_east(i) = P(i+1, t);
            end
        end
        % Calculate residual for each cells
        res = residual(P_west, P_cell, P_east, P(:,t-1), dx,dt,eta);
        n = n+1;
        % Stop iteration if more than iteration limit (maxiter).
        if n >= maxiter
            break
        end
    end
    disp("Max abs(res): " + max(abs(res)))
end

% Plotting
P = [P_Left'; P(:,2:end)];
plot(P(:,:))

% Calculate residual 
function res = residual(P_west, P_cell, P_east, P_cell_prev, dx, dt, eta)
	res = alpha(P_cell, P_east, P_west, dx).*P_east - ...
         beta(P_cell, P_cell_prev, dx, dt, eta).*P_cell + ...
         gamma(P_cell, P_east, P_west, dx).*P_west;
end
% Calculate alpha
function a = alpha(P_cell, P_east, P_west, dx)
	a = ((P_west./(mu_gas(P_west).*z_factor(P_west))) + 4*(P_cell./(mu_gas(P_cell).*z_factor(P_cell))) - ...
		(P_east./(mu_gas(P_east).*z_factor(P_east)))) ./ (4*dx^2);
end
% Calculate beta
function b = beta(P_cell, P_cell_prev, dx, dt, eta)
	b = 2*(P_cell./(mu_gas(P_cell).*z_factor(P_cell)))./ (dx^2) + ...
		(1./(eta*dt)) .* ((1./z_factor(P_cell)) - (P_cell_prev./(P_cell.*z_factor(P_cell_prev))));
end
% Calculate gamma
function g = gamma(P_cell, P_east, P_west, dx)
	g = (-(P_west./(mu_gas(P_west).*z_factor(P_west))) + 4*(P_cell./(mu_gas(P_cell).*z_factor(P_cell))) + ...
		(P_east./(mu_gas(P_east).*z_factor(P_east)))) ./ (4*dx^2);
end
% Calculate gas viscosity
function mu = mu_gas(p)
% Gas viscosity (Gonzalez, Bukacek and Lee, 1967)
    press = [2000:500:5000 6000];
    visc = [0.0164 0.0174 0.0186 0.0197 0.0209 0.0220 0.0233 0.0257];
    fit = polyfit(press,visc,1);
    mu = polyval(fit,p);
end
% Calculate Z-factor
function z_fact = z_factor(p)
    % Papay correlation
    T = 679.7; % 220 F
    Pc = 673; Tc = 344; % Critical properties of methane
    ppr = p/Pc; tpr = T/Tc;
    z_fact = 1 - ((3.53*ppr)/(10.^(0.9813*tpr))) + ((0.274*ppr.^2)/(10.^(0.815*tpr)));
end
