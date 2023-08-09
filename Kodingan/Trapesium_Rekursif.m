clear;
clc;

f = @(x) sin(x);
a = 0;
b = pi;
eps = 10^-3;
MaxIter = 50;
status = 1;

k = 1;
n = 2^(k-1);
h = (b-a)/n;
T = (h/2)*(f(a)+f(b));

while status == 1
    k = k + 1;
    n = 2^(k-1);
    h2 = h;
    h = h/2;
    x = a + h;
    s = 0;
    
    for i=1:n/2
        s = s + f(x);
        x = x + h2;
    end
    
    Tbaru = (T/2) + h*s;
    
    if abs((Tbaru - T)/Tbaru) < eps
        status = 0;
    end
    
    if k >= MaxIter
        display('Proses belum konvergen');
        status = 0;
    end
    
    T = Tbaru;
end

T