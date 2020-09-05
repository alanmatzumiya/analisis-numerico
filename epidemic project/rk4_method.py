import numpy as np
import matplotlib.pyplot as plt

def T(x, t, a, b, c ,d ,e ,f , g, h, i, CHV):
    SH = x[0]
    EH = x[1]
    IH = x[2]
    RH = x[3]
    SV = x[4]
    EV = x[5]
    IV = x[6]

    N = (SH + EH + IH + RH)

    f1 = a - CHV * (IV / N) * SH - b * SH
    f2 =  CHV * (IV / N) * SH - (c + b) * EH
    f3 = c * EH - (d + b + e) * IH
    f4 = d * IH - b * RH
    f5 = f - CHV * (IH / N) * SV - g * SV
    f6 = CHV * (IH / N) * SV - (h + g) * EV
    f7 = h * EV - (g + i) * IV
    return np.array([f1, f2, f3, f4 , f5, f6, f7])

print "t".center(10), "SH(t)".center(14), "EH(t)".center(12), "IH(t)".center(3), "RH(t)".center(14), "SV(t)".center(8), "EV(t)".center(15), "IV(t)".center(8)

def RK4(t0, tf, p, CHV1, CHV2):

    a =  140.0
    b = (1.0 / 3494.0 )
    c = 1.4
    d = 1.0
    e = 0.0035
    f = 28000.0
    g = 0.5
    h = 1.4
    i = 0.01

    CHV1 = 8.1897
    CHV2 = 0.9523

    SH0 = 1000000.0
    EH0 = 15.0
    IH0 = 3.0
    RH0 = 0.0
    SV0 = 100000.0
    EV0 = 60.0
    IV0 = 20.0


    X0 =[SH0, EH0, IH0, RH0, SV0, EV0, IV0]

    t0 = 0
    tf = 35
    t = np.linspace(t0, tf, 1000)
    p = t[1] - t[0]

    RK4 = np.zeros([t.shape[0], 7])
    RK4[0] = X0
    tn = t0


    for j in np.arange(t.shape[0] - 1):

        if tn < 8.0:
            t[j] = t[0] + p * j
            tn = t[j]
            CHV = CHV1
            k1 = T(RK4[j], t[j], a, b, c ,d ,e ,f , g, h, i, CHV)
            k2 = T(RK4[j] + 0.5 * k1 * p, t[j], a, b, c ,d ,e ,f , g, h, i, CHV)
            k3 = T(RK4[j] + 0.5 * k2 * p, t[j], a, b, c ,d ,e ,f , g, h, i, CHV)
            k4 = T(RK4[j] + k3 * p, t[j], a, b, c ,d ,e ,f , g, h, i, CHV)

            RK4[j + 1] = RK4[j] + (1.0 / 6.0) * p * (k1 + 2 * k2 + 2 * k3 + k4)

        else:
            CHV = CHV2
            RK4[j + 1] = RK4[j] +  p * T(RK4[j], t[j], a, b, c ,d ,e ,f , g, h, i, CHV)

            k1 = T(RK4[j], t[j], a, b, c, d, e, f, g, h, i, CHV2)
            k2 = T(RK4[j] + 0.5 * k1 * p, t[j], a, b, c, d, e, f, g, h, i, CHV)
            k3 = T(RK4[j] + 0.5 * k2 * p, t[j], a, b, c, d, e, f, g, h, i, CHV)
            k4 = T(RK4[j] + k3 * p, t[j], a, b, c, d, e, f, g, h, i, CHV)

            RK4[j + 1] = RK4[j] + (1.0 / 6.0) * p * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.array(RK4)

t0 = 0
tf = 35
t = np.linspace(t0, tf, 1000)
p = t[1] - t[0]
CHV1 = 8.1897
CHV2 = 0.9523

RK4 = RK4(t0, tf, p, CHV1, CHV2)

x1 = RK4[:,0]
x2 = RK4[:,1]
x3 = RK4[:,2]
x4 = RK4[:,3]
x5 = RK4[:,4]
x6 = RK4[:,5]
x7 = RK4[:,6]

col1 = [] ; col2 = [] ; col3 = [] ; col4 = [] ; col5 = [] ; col6 = [] ; col7 = [] ; col8 = []
col9 = [] ; col10 = [] ; col11 = [] ; col12 = [] ; col13 = [] ; col14 = [] ; col15 = [] ; col16 = []

tn = t0
for i in np.arange(t.shape[0]):
    if tn < 8:
        tn = t[i]
        col1.append(tn); col2.append(x1[i]) ; col3.append(x2[i]) ; col4.append(x3[i]) ; col5.append(x4[i])
        col6.append(x5[i]) ; col7.append(x6[i]) ; col8.append(x7[i])
        print '{0: 4f} {1: 4f} {2: 4f} {3: 4f} {4: 4f} {5: 4f} {6: 4f} {7: 4f}'.format(tn, x1[i], x2[i], x3[i], x4[i],x5[i], x6[i], x7[i])
    else:
        tn = t[i]
        col9.append(tn); col10.append(x1[i -1]); col11.append(x2[i -1]); col12.append(x3[i -1]); col13.append(x4[i -1])
        col14.append(x5[i -1]); col15.append(x6[i -1]); col16.append(x7[i -1])
        print '{0: 4f} {1: 4f} {2: 4f} {3: 4f} {4: 4f} {5: 4f} {6: 4f} {7: 4f}'.format(tn, x1[i], x2[i], x3[i],
                                                                               x4[i], x5[i], x6[i], x7[i])

plt. figure(1)
plt.plot(col1, col2, label = 'CHV = 8.1897')
plt.plot(col9, col10, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes susceptibles, SH(t)')
plt.legend(loc=0)

plt. figure(2)
plt.plot(col1, col3, label = 'CHV = 8.1897')
plt.plot(col9, col11, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes expuestos, EH(t)')
plt.legend(loc=0)

plt. figure(3)
plt.plot(col1, col4, label = 'CHV = 8.1897')
plt.plot(col9, col12, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes infectados, IH(t)')
plt.legend(loc=0)

plt. figure(4)
plt.plot(col1, col5, label = 'CHV = 8.1897')
plt.plot(col9, col13, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de huespedes recuperados, RH(t)')
plt.legend(loc=0)

plt. figure(5)
plt.plot(col1, col6, label = 'CHV = 8.1897')
plt.plot(col9, col14, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de vectores susceptibles, SV(t)')
plt.legend(loc=0)

plt. figure(6)
plt.plot(col1, col7, label = 'CHV = 8.1897')
plt.plot(col9, col15, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de vectores expuestos, EV(t)')
plt.legend(loc=0)

plt. figure(7)
plt.plot(col1, col8, label = 'CHV = 8.1897')
plt.plot(col9, col16, label = 'CHV = 0.9523')
plt.xlabel('t (semanas)')
plt.ylabel('Poblacion total de vectores infectados, IV(t)')
plt.legend(loc=0)

plt.show()


