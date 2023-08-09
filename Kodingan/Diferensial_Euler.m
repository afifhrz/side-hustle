clc;
clear;

f = @(t,y) (t-y)/2; %y'
a = 0;              
b = 5;
h = 0.5;            %panjang partisi
y = 1;              %y(a)

n = (b-a)/h;
t = a;

for i = 1:n
    y = y + h*f(t,y);
    t = t + h;
end

y