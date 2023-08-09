clear; clc;

M = [
    4, -2, 2;
    -2, 2, -3;
   2, -3, 14];

n = length(M);

L = eye(n);
U = zeros(n,n);

for k = 1:n
    for i = k:n
        s = 0;
        for j = 1:k-1
            s = s + L(k,j)*U(j,i);
        end
        
        U(k,i) = M(k,i)-s;
    end
    
    for i = k+1:n
        s = 0;
        for j = 1:k-1
            s = s + L(i,j)*U(j,k);
        end
        
        L(i,k) = (M(i,k) - s)/U(k,k);
    end
end
