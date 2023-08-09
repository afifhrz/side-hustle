clc;
clear all;
A = [2, 5, -4, -5, -2;
    -2, 1, -7, 6, 3;
    8, 4, 16, -4, 24;
    1, 1.5, 3, 4.5, 16;];
%%
n=6;
s=0;
D=0;
l=1;
eps=10^-6;
for k=1:n-1
    m=k;
    for i=k+1:n
        if abs(A(i,k))>abs(A(m,k))
           m=i;
        end
    end
    if m~=k
        l=-1*l
        for j=k:n
            s=A(k,j);
            A(k,j)=A(m,j);
            A(m,j)=s;
        end
    end
    for i = k+1:n
        p = A(i,k)/A(k,k)
            for j = k+1:n+1
                A(i,j)= A(i,j)- p*A(k,j)
            end
        A(i,k)=0    
    end
end
A
%%
D=1
for i=1:n
        D=D*A(i,i)
end
D=D*l