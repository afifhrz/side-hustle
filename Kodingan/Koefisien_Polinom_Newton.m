clear; clc;

a = [0, 1, 2, 3, 4];
f = [1, 5, 31, 121, 341];

n = length(a);
b = f;

c(1) = b(1);

for k = 1:n-1
    for i = 1:n-k
       b(i) = (b(i+1) - b(i))/(a(i+k) - a(i));
    end
    
    c(k+1) = b(1);
end