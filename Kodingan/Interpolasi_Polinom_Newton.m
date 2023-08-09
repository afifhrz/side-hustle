clear; clc;

% x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5];
% y = [0.95, 0.8001, 0.5517, 0.2128, -0.1890, -0.5813, -0.8066, -0.5616, 0.6867, 3.8125];

x = [-1, 4, -0.5, 2, 0, 3, 0.5, 1, 1.5, 2.5, 3.5];
y = [2.7183, 0.2931, 0.4122, 0.5413, 0, 0.4481, 0.1516, 0.1517, 0.5020, 0.5130, 0.3699];

eps = 10^-4;
n = length(x);
status = 1;

%akan menaksir
z = 0.75;

p = y(1);
b(1) = y(1);
FAKTOR = 1;
k = 2;

while status == 1
    b(k) = y(k);
    for i = k-1:-1:1
        b(i) = (b(i+1) - b(i))/(x(k) - x(i));
    end
    
    FAKTOR = FAKTOR*(z - x(k-1));
    SUKU = b(1)*FAKTOR;
    
    p = p + SUKU;
    
    if abs(SUKU/p) < eps
        status = 0;
        p
    end
    
    k = k+1;
    
    if k > n
        display('Proses belum konvergen, namun taksiran polinom newtonnya adalah:');
        p
        status = 0;
    end
end