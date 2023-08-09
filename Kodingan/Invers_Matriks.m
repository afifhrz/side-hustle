clear; clc;

M = [
    4, -5, -2.5, -0.5;
    -2, 2, -3, 1;
    -2, -4.5, 2.5, -5;
    4.5, 1, -3.5, 3];

n = length(M);

MM = [M, eye(n)];

Pivoting = 1; %1 untuk menggunakan Pivoting dan 0 untuk tidak
status = 1; %Parameter kegagalan proses
k = 1;

while status == 1 && k<=n
    if Pivoting == 1
        m = k;
        for i = k+1:n
            if abs(MM(i,k)) > abs(MM(m,k))
                m = i;
            end
        end
        if m~=k
            for j = k:2*n
                s = MM(k,j);
                MM(k,j) = MM(m,j);
                MM(m,j) = s;
            end
        end
    end
    
    p = MM(k,k);
    
    for j = k:2*n
        MM(k,j) = MM(k,j)/p;
    end
    
    if abs(MM(k,k)) < 10^-12
        display('Proses Gagal');
        status = 0;
    end
    
    if status == 1
        for i=1:n
            if i ~= k
                p = MM(i,k)/MM(k,k);
                for j=k+1:2*n
                    MM(i,j) = MM(i,j) - p*MM(k,j);
                end
                MM(i,k) = 0;
            end
        end
        
        k = k+1;
    end
end

Minv = MM(:, n+1:2*n)