clc;
clear;

f = @(t,y) (t-3*y)/2; %y'
a = 0;              
b = 3;
h = 0.25;            %panjang partisi
y(1) = 1;              %y(a)

n = (b-a)/h;
t(1) = a;

for i = 1:n
    ttengah = t(i) + h/2;
    tbaru = t(i) + h;
    K1 = h*f(t(i),y(i));
    K2 = h*f(ttengah, y(i) + K1/2);
    K3 = h*f(ttengah, y(i) + K2/2);
    K4 = h*f(tbaru, y(i) + K3);
    y(i+1) = y(i) + (1/6)*(K1 + 2*K2 + 2*K3 + K4);
    t(i+1) = tbaru;
end

y
plot (t,y)