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
    p = y + h*f(t,y);
    tbaru = t + h;
    y = y + (h/2)*(f(t,y) + f(tbaru,p));
    t = tbaru;
end

y