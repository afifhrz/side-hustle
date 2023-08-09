clear; clc;

M = [
    3, 4, 5, 6;
    1, 2, 3, 4;
    3, 7, 6, 3;
    4, 5, 6, 9];

n = length(M);

L = zeros(n,n);
U = eye(n);

for k = 1:n
    for i = k:n
        s = 0;
        for j = 1:k-1
            s = s + L(i,j)*U(j,k);
        end
        
        L(i,k) = M(i,k)-s;
    end
    
    for i = k+1:n
        s = 0;
        for j = 1:k-1
            s = s + L(k,j)*U(j,i);
        end
        
        U(k,i) = (M(k,i) - s)/L(k,k);
    end
end