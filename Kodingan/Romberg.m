clear;
clc;

f = @(x) (sin(x))^2 / x^2;
a = 0.001;
b = pi;
eps = 10^-5;
maxiter = 10;

status = 1;

h = b-a;
R(1,1) = h/2 * (f(a) + f(b));
j = 2;

while status == 1
    n = 2^(j-1);
    h2 = h;
    h = h/2;
    s = 0;
    x = a + h;
    
    for i = 1:(n/2)
        s = s + f(x);
        x = x + h2;
    end
    
    R(j,1) = (R(j-1,1)/2) + h*s;
    
    for k = 2:j
        R(j,k) = ((4^(k-1)*R(j,k-1))-R(j-1,k-1))/(4^(k-1) - 1);
    end
    
    if abs((R(j,j) - R(j-1,j-1))/R(j,j)) < eps
        status = 0;
    end
    
    j = j+1;
    
    if j > maxiter
        status = 0;
        display('Proses belum konvergen');
    end
end

R(j-1,j-1)