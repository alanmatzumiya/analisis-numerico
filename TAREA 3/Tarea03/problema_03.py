import numpy as np
import matplotlib.pyplot as plt


def f(x,t ,v ):
    return(v * x)

def sol_exacta(t):
    s = np.exp(-10 * t)
    return s

print 'Para h = 1 / 6 y h = 1 / 12'
print "n".center(9), "tn".center(2), "Xn".center(15)

H = [1.0 / 6.0, 1.0 / 12.0]
for j in H:

    t0 = 0
    x0 = 1
    v = - 10.0
    t = []
    t.append(t0)
    euler = []
    euler.append(x0)
    tn = t[0]
    N = [0, 1 , 2 , 3]
    for i in N:
        tn = t[0] + j * (i + 1)
        t.append(tn)
        x1 = x0 + j * f(x0, tn, v)
        euler.append(x1)
        x0 = x1
        print '{0: 5d} {1: 5f} {2: 5f} '.format(i, t[i], euler[i])

    plt.figure()
    t_ex = np.linspace(0, 0.5, 200)
    s_exact = sol_exacta(t_ex)
    plt.plot(t, euler, "*")
    plt.plot(t_ex, s_exact)

    plt.show()

print 'Para responder a la ultima pregunta, h tiene que tomar valores menores a 1/10'

