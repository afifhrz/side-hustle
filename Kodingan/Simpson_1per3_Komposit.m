clear;
clc;

f = @(x) sin(x);
a = 0;
b = pi;
n = 50; %banyak partisi, harus genap

h = (b-a)/n; %panjang partisi

x = a;
s = f(x);

for i = 1:n-1
    x = x + h;
    if mod(i,2) == 1
        s = s + 4*f(x);
    else
        s = s + 2*f(x);
    end
end

x = x + h;
s = s + f(x);

int = (h/3)*s