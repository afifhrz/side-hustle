clear;
clc;

f = @(x) sin(x);
a = 0;
b = pi;
n = 50; %banyak partisi

h = (b-a)/n; %panjang partisi

x = a;
s = f(x);

for i = 1:n-1
    x = x + h;
    s = s + 2*f(x);
end

x = x + h;
s = s + f(x);

int = (h/2)*s

