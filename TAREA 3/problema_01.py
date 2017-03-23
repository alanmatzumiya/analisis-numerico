import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return(1 - 2 * t) * x

def sol_exacta(t):
    s = np.exp(0.25 - (0.5 - t)**2)
    return s


def euler_method(n_max = 6 , x0 = 1.0):
    t = np.linspace(0, 3, n_max)
    n_size = t.shape[0]
    x = np.zeros(n_size)
    h = t[1] - t[0]

    x[0] = x0

    for j in np.arange(n_size - 1):
        x[j + 1] = x[j] + h * f(x[j], t[j])
    return x


print "n".center(10), "h".center(2), "Xn".center(13), "GEs".center(8), "GE/h".center(6)

col1 = []
col2 = []
col3 = []
col4 = []
N = [10.0, 20.0, 40.0]
j = 1
for i in N:
    t_ex = np.linspace(0, 3, 201)
    p = np.float(3 / i)
    col1.append(p)
    x_euler = euler_method(i + 1, 1.0)
    x_euler_i = x_euler[3*j]
    col2.append(x_euler_i)
    x_exacta = sol_exacta(t_ex)[60]
    GE = x_exacta - x_euler_i
    col3.append(GE)
    F = np.float(GE / p)
    col4.append(F)
    j = 2*j

i = 0
j = 1
for i in np.arange(i,3):
    print '{0: 5d} {1: 5f} {2: 5f} {3: 5f} {4: 5f}'.format(3*j, col1[i], col2[i], col3[i], col4[i])
    j = 2*j


fig_1 = plt.figure()
t_ex = np.linspace(0, 3, 200)
t_euler_1 = np.linspace(0 ,3 , 10)
x_euler_1 = euler_method(10, 1.0)
s_exact = sol_exacta(t_ex)
plt.plot(t_euler_1 , x_euler_1, "*")
plt.plot(t_ex, s_exact)

fig_2 = plt.figure()
t_ex = np.linspace(0, 3, 200)
t_euler_2 = np.linspace(0 ,3 , 20)
x_euler_2 = euler_method(20, 1.0)
s_exact = sol_exacta(t_ex)
plt.plot(t_euler_2 , x_euler_2, "*")
plt.plot(t_ex, s_exact)

fig_3 = plt.figure()
t_ex = np.linspace(0, 3, 200)
t_euler_3 = np.linspace(0 ,3 , 40)
x_euler_3 = euler_method(40, 1.0)
s_exact = sol_exacta(t_ex)
plt.plot(t_euler_3 , x_euler_3, "*")
plt.plot(t_ex, s_exact)

plt.show()
