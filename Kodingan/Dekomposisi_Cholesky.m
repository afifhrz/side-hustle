clear; clc;

M = [
    3, 1, 3, 6;
    1, 2, 3, 4;
    3, 3, 6, 6;
    6, 4, 6, 9];
% M harus simetris

n = length(M);

L = zeros(n,n);
U = zeros(n,n);

for k = 1:n
    s = 0;
    for j = 1:k-1
        s = s + L(k,j)^2;
    end
    
    L(k,k) = sqrt(M(k,k) - s);
    
    for i = k+1:n
        s = 0;
        for j = 1:k-1
            s = s + L(k,j)*L(i,j);
        end
        
        L(i,k) = (M(i,k)-s)/L(k,k);
    end
    
    for i = k:n
        U(k,i) = L(i,k);
    end
end