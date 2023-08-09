clc
clear all
A = [4,-6,1,;
    8,2,-3;
    3,-4,10;];
B=eye(3,3);
C=[A,B];
n=3;
for k=1:n-1
    m=k;
    for i=k+1:n
        if abs (C(i,k)) > abs (C(m,k))
            m=i;
        end
    end
    if m~=k
        for j=1:n+3
            s=C(k,j);
            C(k,j)=C(m,j);
            C(m,j)=s;
        end
    end
    for i=k+1:n
        p=C(i,k)/C(k,k);
        for j=1:n+3
            C(i,j)=C(i,j)-p*C(k,j);
            C(i,k)=0;
        end
    end
end
C

%%
for k=n:-1:2
    for i=k-1:-1:1
        p=C(i,k)/C(k,k);
        for j=1:n+3
            C(i,j)=C(i,j)-p*C(k,j);
            C(i,k)=0;
        end
    end
end
C
%%
for i=1:n
    for j=n+3:-1:1
            C(i,j)=C(i,j)/C(i,i);
    end
end
C
%%
A^-1