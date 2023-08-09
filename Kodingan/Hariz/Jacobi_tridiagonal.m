clc
clear all
C=randi(10,6);
C=tril(C,1);
C=transpose(C);
C=tril(C,1);
B=randi(10,[6,1]);
%%
clc
n=6;
A=[C,B]
eps = 10^-6;
for k=1:n-1
    if abs(A(k,k))<eps
        return
    end
    p=A(k+1,k)/A(k,k);
    A(k+1,k)=A(k+1,k)-p*A(k,k);
    A(k+1,n+1)=A(k+1,n+1)-p*A(k,n+1);
    A(k+1,k)=0;
end
if abs(A(k,k)) < eps
    display("Koef Singular");
    return
end
%% 
Y=[-5,-5,-5,-5,-5,-5];
galat=[0,0,0,0,0,0];
status=1;
silon=0.05;
iter=0;
A=[C,B];
D=diag(A);
while status==1
    for i=1:n
        s=0;
        for j=1:n
            if j~=i
                s=s+A(i,j)*Y(j);
            end
        end
        Ybaru(i)=(A(i,n+1))-s/D(i);
        s=abs ((Ybaru(i)-Y(i))/Ybaru(i));
        if s>galat(i)
            galat(i)=s;
        end
    end
    for i=1:n
        Y(i)=Ybaru(i);
    end
    if max(galat)<silon || iter>1
        status=0;
    end
    iter=iter+1;
end