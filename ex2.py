import numpy as np
from scipy.constants import hbar

E1 = 1
E2 = 1
V = 1
c0 = np.array([[1], [0]])
h = 0.1
H = np.array([[E1, V], [V, E2]])

def c(n):
    def f(H):
      return complex(0, -1/hbar)*np.dot(H, c(n))
    k1 = f(H,c(n-1))
    k2 = f(H, (c(n-1) + h*k1/2))
    k3 = f(H, (c(n-1) + h*k2/2))
    k4 = f(H, (c(n-1) + h*k3/2))
    if n == 0:
        return c0
    else:
        return y(n-1) + h*(k1 + 2*k2 + 2*k3 + k4)/6

c1r, c1i, c2r, c2i = [], [], [], []
for i in range(500):
    c1r.append(c[0, 0].real)
    c1i.append(c[0, 0].imag)
    c2r.append(c[1, 0].real)
    c1i.append(c[1, 0].imag)