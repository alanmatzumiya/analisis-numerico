import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return( 2 * x * ( 1 - x ) )

def sol_exacta(t):
    s = 1 / (1 + 4 * (np.exp(2 * (10 - t))))
    return s

print "n".center(10), "tn".center(2), "Xn".center(15), "xn'".center(6)

def euler_method(n_max = 16 , x0 = 0.2):
    t = np.linspace(10, 13, n_max)
    n_size = t.shape[0]
    x = np.zeros(n_size)
    h = 0.2

    x[0] = x0
    col1 = []
    col2 = []
    col3 = []
    for j in np.arange(n_size - 1):
        tn = t[0] + h * j
        col1.append(tn)
        x[j + 1] = x[j] + h * f(x[j], t[j])
        col2.append(x[j])
        xn_prima = f(x[j], t[j])
        col3.append(xn_prima)

        print '{0: 5d} {1: 5f} {2: 5f} {3: 5f}'.format(j, col1[j], col2[j], col3[j])

    return x

fig = plt.figure()
t_ex = np.linspace(10, 13, 200)
t_euler = np.linspace(10, 13  , 16)
x_euler = euler_method(16, 0.2)
s_exact = sol_exacta(t_ex)
plt.plot(t_euler , x_euler, "*")
plt.plot(t_ex, s_exact)

plt.show()

