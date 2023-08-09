clc;
clear;

f = @(t,y) (t-y)/2; %y'
a = 0;
b = 5;
h = 0.5;            %panjang partisi
y = 1;              %y(a)

n = (b-a)/h;
t = a;

y0 = y;
t0 = a;
for i = 1:n
    if i <= 3
        ttengah = t + h/2;
        tbaru = t + h;
        K1 = h*f(t,y);
        K2 = h*f(ttengah, y + K1/2);
        K3 = h*f(ttengah, y + K2/2);
        K4 = h*f(tbaru, y + K3);
        y = y + (1/6)*(K1 + 2*K2 + 2*K3 + K4);
        t = tbaru;
        if i == 1
            y1 = y;
            t1 = t;
        elseif i == 2
            y2 = y;
            t2 = t;
        else
            y3 = y;
            t3 = t;
        end
    else
        t = t+h;
        p = y0 + (4*h/3)*(2*f(t1,y1) - f(t2,y2) + 2*f(t3,y3));
        y = (-y1 + 9*y3)/8 + (3*h/8)*(-f(t2,y2) + 2*f(t3,y3) + f(t,p));
        
        t0 = t1;
        t1 = t2;
        t2 = t3;
        t3 = t;
        
        y0 = y1;
        y1 = y2;
        y2 = y3;
        y3 = y;
    end
end

y