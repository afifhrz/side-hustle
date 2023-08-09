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
    xbaru = x + h*f(t,x,y);
    ybaru = y + h*g(t,x,y);
    t = t + h;
    x = xbaru;
    y = ybaru;
end

x
y