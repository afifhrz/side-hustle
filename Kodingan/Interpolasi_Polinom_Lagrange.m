clear; clc;

% x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5];
% y = [0.95, 0.8001, 0.5517, 0.2128, -0.1890, -0.5813, -0.8066, -0.5616, 0.6867, 3.8125];

x = [-1,4, -0.5, 2, 0, 3, 0.5, 1, 1.5, 2.5, 3.5];
y = [2.7183, 0.2931, 0.4122, 0.5413, 0, 0.4481, 0.1516, 0.1517, 0.5020, 0.5130, 0.3699];

n = length(x);

%akan menaksir
z = 0.75;

p = 0;

for i = 1:n
    L = 1;
    for j = 1:n
        if j ~= i
            L = L*(z - x(j))/(x(i) - x(j));
        end
    end
    p = p + y(i)*L;
end

p