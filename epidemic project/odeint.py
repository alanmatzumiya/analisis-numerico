import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def T(x, t):
    SH = x[0]
    EH = x[1]
    IH = x[2]
    RH = x[3]
    SV = x[4]
    EV = x[5]
    IV = x[6]

    N = SH + EH + IH + RH

    f1 = a - CHV * (IV / N) * SH - b * SH
    f2 =  CHV * (IV / N) * SH - (c + b) * EH
    f3 = c * EH - (d + b + e) * IH
    f4 = d * IH - b * RH
    f5 = f - CHV * (IH / N) * SV - g * SV
    f6 = CHV * (IH / N) * SV - (h + g) * EV
    f7 = h * EV - (g + i) * IV
    return np.array([f1, f2, f3, f4 , f5, f6, f7])

print "t".center(10), "SH(t)".center(14), "EH(t)".center(12), "IH(t)".center(3), "RH(t)".center(14), "SV(t)".center(8), "EV(t)".center(15), "IV(t)".center(8)

a = 140.0
b = (1.0 / 3494.0 )
c = 1.4
d = 1.0
e = 0.0035
f = 28000.0
g = 0.5
h = 1.4
i = 0.01

SH0 = 1000000.0
EH0 = 15.0
IH0 = 3.0
RH0 = 0.0
SV0 = 100000.0
EV0 = 60.0
IV0 = 20.0

X0 =[SH0, EH0, IH0, RH0, SV0, EV0, IV0]

CHV1 = 8.1897
CHV = CHV1
t0 = 0
t1 = 8
tk = np.linspace(t0, t1, 1000)

solode = odeint(T, X0, tk)
x1 = solode[:, 0] ; x2 = solode[:, 1] ; x3 = solode[:, 2] ; x4 = solode[:, 3] ; x5 = solode[:, 4]
x6 = solode[:, 5] ; x7 = solode[:, 6]

for i in np.arange(tk.shape[0]):
    tn = tk[i]
    print '{0: 4f} {1: 4f} {2: 4f} {3: 4f} {4: 4f} {5: 4f} {6: 4f} {7: 4f}'.format(tn, x1[i], x2[i], x3[i], x4[i],x5[i], x6[i], x7[i])

SH0 = solode[:, 0][len(tk) - 1]
EH0 = solode[:, 1][len(tk) - 1]
IH0 = solode[:, 2][len(tk) - 1]
RH0 = solode[:, 3][len(tk) - 1]
SV0 = solode[:, 4][len(tk) - 1]
EV0 = solode[:, 5][len(tk) - 1]
IV0 = solode[:, 6][len(tk) - 1]

Y0 = [SH0, EH0, IH0, RH0, SV0, EV0, IV0]

CHV2 = 0.9523
CHV = CHV2
t2 = 8
tf = 35
t = np.linspace(t2, tf, 1000)

solode = odeint(T, Y0, t)
y1 = solode[:, 0] ; y2 = solode[:, 1] ; y3 = solode[:, 2] ; y4 = solode[:, 3] ; y5 = solode[:, 4]
y6 = solode[:, 5] ; y7 = solode[:, 6]

for i in np.arange(t.shape[0]):
    tn = t[i]
    print '{0: 4f} {1: 4f} {2: 4f} {3: 4f} {4: 4f} {5: 4f} {6: 4f} {7: 4f}'.format(tn, y1[i], y2[i], y3[i], y4[i],y5[i], y6[i], y7[i])


plt. figure(1)
plt.plot(tk, x1, label = 'CHV = 8.1897')
plt.plot(t, y1, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes susceptibles, SH(t)')
plt.legend(loc=0)

plt. figure(2)
plt.plot(tk, x2, label = 'CHV = 8.1897')
plt.plot(t, y2, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes expuestos, EH(t)')
plt.legend(loc=0)

plt. figure(3)
plt.plot(tk, x3, label = 'CHV = 8.1897')
plt.plot(t, y3, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes infectados, IH(t)')
plt.legend(loc=0)

plt. figure(4)
plt.plot(tk, x4, label = 'CHV = 8.1897')
plt.plot(t, y4, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes recuperados, RH(t)')
plt.legend(loc=0)

plt. figure(5)
plt.plot(tk, x5, label = 'CHV = 8.1897')
plt.plot(t, y5, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de vectores susceptibles, SV(t)')
plt.legend(loc=0)

plt. figure(6)
plt.plot(tk, x6, label = 'CHV = 8.1897')
plt.plot(t, y6, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de vectores expuestos, EV(t)')
plt.legend(loc=0)

plt. figure(7)
plt.plot(tk, x7, label = 'CHV = 8.1897')
plt.plot(t, y7, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de vectores infectados, IV(t)')
plt.legend(loc=0)

plt.show()
