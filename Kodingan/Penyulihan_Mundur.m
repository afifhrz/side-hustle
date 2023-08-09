clear; clc;

M = [
1, 5, -4, -5, -2;
0, 11, -15, -4, -1;
0, 0, -1.0909, 22.9091, 36.7273;
0, 0, 0, 55, 92.667]; % Matriks Segitiga Atas

n = length(M)-1;
status = 1;
k = n-1;

if abs(M(n,n)) < 10^-12
   display('Proses Gagal');
   status = 0;
end

x(n) = M(n,n+1)/M(n,n);

while status == 1 && k>0
   if abs(M(k,k)) < 10^-12
       display('Proses Gagal');
       status = 0;
   end
   
   if status == 1
      s = 0;
      for i = k+1:n
         s = s + M(k,i)*x(i); 
      end
      
      x(k) = (M(k,n+1) - s)/M(k,k);
   end
    
   k = k-1;
end