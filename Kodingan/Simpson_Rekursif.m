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
T1 = (h/2)*(f(a)+f(b));

k = 2;
n = 2^(k-1);
h = h/2;
T = (T1/2) + h*f(a+h);

S = (4*T - T1)/3;

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
    Sbaru = (4*Tbaru - T)/3;
    
    if abs((Sbaru - S)/Sbaru) < eps
        status = 0;
    end
    
    if k >= MaxIter
        display('Proses belum konvergen');
        status = 0;
    end
    
    T = Tbaru;
    S = Sbaru;
end

S