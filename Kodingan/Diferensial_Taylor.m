clc;
clear;

f{1} = @(t,y) (t-y)/2;
f{2} = @(t,y) (1/2) - f{1}(t,y)/2;
a = 0;              
b = 5;
h = 0.5;            %panjang partisi
y = 1;              %y(a)
