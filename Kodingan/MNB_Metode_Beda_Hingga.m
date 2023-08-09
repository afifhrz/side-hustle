clc;
clear;

%PD: x'' = p(t) x' + q(t) x + r(t)

p = @(t) 0;
q = @(t) 0;
r = @(t) 1;

a = -2;
b = 2;

h = 0.01;

n = (b-a)/h;

x(1) = 1;   %diberi soal
x(n+1) = 1;  %diberi soal

t(1) = a;
t(n+1) = b;

t(2) = t(1) + h;
b(2) = (-h^2)*r(t(2)) + ((h/2)*p(t(2)) + 1)*x(1);
d(2) = 2 + (h^2)*q(t(2));
c(2) = (h/2)*p(t(2)) - 1;

for i = 3:n-1
   t(i) = t(i-1) + h;
   a(i) = (-h/2)*p(t(i)) - 1;
   d(i) = 2 + (h^2)*q(t(i));
   c(i) = (h/2)*p(t(i)) - 1;
   b(i) = (-h^2)*r(t(i));
end

t(n) = t(n-1) + h;
a(n) = (-h/2)*p(t(n));
d(n) = 2 + (h^2)*q(t(n));
b(n) = (-h^2)*r(t(n)) - ((h/2)*p(t(n)) - 1)*x(n+1);

%Penyelesaian tridiagonal
for k = 2:n-1
   pembagi = a(k+1)/d(k);
   d(k+1) = d(k+1) - pembagi*c(k);
   b(k+1) = b(k+1) - pembagi*b(k);
   a(k+1) = 0;
end

x(n) = b(n)/d(n);

for k = n-1:-1:2
   x(k) = (b(k) - c(k)*x(k+1))/d(k);
end

x
plot(t,x)