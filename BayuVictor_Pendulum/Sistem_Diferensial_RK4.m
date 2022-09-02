clear;
clc;

f = @(t,x,y) x - y;
g = @(t,x,y) cos(t) -5*x -4*y;

a = 0;
b = 1;
h = 0.1;
x = 3;
y = -5;

n = (b-a)/h;
t = a;

for i = 1:n
    tbaru = t+h;
    ttengah = t + h/2;
    
    K1 = h*f(t,x,y);
    L1 = h*g(t,x,y);
    
    K2 = h*f(ttengah, x + K1/2, y + L1/2);
    L2 = h*g(ttengah, x + K1/2, y + L1/2);
    
    K3 = h*f(ttengah, x + K2/2, y + L2/2);
    L3 = h*g(ttengah, x + K2/2, y + L2/2);
    
    K4 = h*f(tbaru, x + K3, y + L3);
    L4 = h*g(tbaru, x + K3, y + L3);
    
    x = x + (1/6)*(K1 + 2*K2 + 2*K3 + K4);
    y = y + (1/6)*(L1 + 2*L2 + 2*L3 + L4);
    t = tbaru;
end

x
y