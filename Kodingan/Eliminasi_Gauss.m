clear all; clc;

M = [
    2, 5, -4, -5, -2;
    -2, 1, -7, 6, 3;
    8, 4, 16, -4, 24;
    1, 1.5, 3, 4.5, 16;];

Pivoting = 1; %1 untuk menggunakan Pivoting dan 0 untuk tidak
Determinan = 1; %1 untuk menghitung determinan dan 0 untuk tidak
Row_Change = 0;

n = length(M)-1;
status = 1; %Parameter kegagalan proses
k = 1;

while status == 1 && k<n
    if Pivoting == 1
        m = k;
        for i = k+1:n
            if abs(M(i,k)) > abs(M(m,k))
                m = i;
            end
        end
        if m~=k
            Row_Change = Row_Change + 1;
            for j = k:n+1
                s = M(k,j);
                M(k,j) = M(m,j);
                M(m,j) = s;
            end
            
        end
    end
    
    if abs(M(k,k)) < 10^-12
        display('Proses Gagal');
        status = 0;
    end
    
    if status == 1
        for i=k+1:n
            p = M(i,k)/M(k,k);
            for j=k+1:n+1
                M(i,j) = M(i,j) - p*M(k,j);
            end
            M(i,k) = 0;
        end
        
        k = k+1;
    end
end

if Determinan == 1
   Det = 1;
   for i = 1:n
      Det = M(i,i)*Det; 
   end
   
   Det = Det*(-1)^Row_Change;
   
   Det
end