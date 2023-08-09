clc
clear all;
A=[1,1,1;0,3,5;0,0,1];
%A= randi(10,6);
%A=tril(A,1);
%A=transpose(A);
%A=tril(A,1);
B=[4,5,1]';
A = [A,B];
%%
n=3;
eps = 10^-6;
for k=1:n-1
    if abs(A(k,k))<eps
        return
    end
    p=A(k+1)/A(k,k);
    A(k+1,k)=A(k+1,k)-p*A(k,k);
    A(k+1,n+1)=A(k+1,n+1)-p*A(k,n+1);
    A(k+1,k)=0;
end
if abs(A(k,k)) < eps
    display("Koef Singular");
    return
end
X(n)=A(n,n+1)/A(n,n);
for k=n-1:-1:1
    X(k)=(A(k,n+1)-A(k,k+1)*X(k+1))/A(k,k);
end