clear; clc;

M = [
    8, 3, -2, 1, 2;
    4, 12, 4, 3, -7;
    2, -2, 9, 3, 10;
    1, 2, 4, 8, -5];

n = length(M)-1;
x = [2,2,6,3]; %Tebakan awal
eps = 10^-6;
maksiter = 50;

status = 1;

iter = 0;

while status == 1
    galat = 0;
    for i = 1:n
        s = 0;
        for j = 1:n
            if j~=i
                s = s + M(i,j)*x(j);
            end
        end
        
        xbaru = (M(i,end) - s)/M(i,i);
        s = abs((xbaru - x(i))/xbaru);
        if s > galat
            galat = s;
        end
        x(i) = xbaru;
    end
    
    if galat < eps
        status = 0;
    end
    
    if status == 1
        iter = iter + 1;
        
        if iter > maksiter
            display('Proses belum konvergen');
            status = 0;
        end
    end
end