

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

plt.style.use(['science', "notebook"])

pa = [-12, 16]
pb = [-6, 10]
pc = [-18, -14]

def f(x, a, b, c):
    a * x**2 + b * x + c

mat1 = np.array([[ pa[0] ** 2, pa[0], 1],
                  [ pb[0] ** 2, pb[0], 1],
                  [ pc[0] ** 2, pc[0], 1]])

mat2 = np.array([ pa[1], pb[1], pc[1] ])

mat3 = np.linalg.solve(mat1, mat2)

x1 = np.linspace(-20,20,200)
y1 = f( x1, mat3[0], mat3[1], mat3[2] )

x2 = np.array([ pa[0], pb[0], pc[0] ])
y2 = np.array([ pa[1], pb[1], pc[1] ])

fig, ax = plt.subplots()

ax.plot(x1,y1)
ax.plot(x2, y2, "o", color = "red")

ax.axhline(y=0, color='k', lw = 1)
ax.axvline(x=0, color='k', lw = 1)

ax.set_ylim(-20,20)
ax.set_xlim(-20,20)
ax.set_aspect("equal", "box")
ax.grid(
        which = "major"
        )
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=10)

ax.set_title(str(round(mat3[0],3)) + "$x ^ 2 + $" +
             str(round(mat3[1],3)) + "$x  + $" +
             str(round(mat3[1],3))
            )

plt.show()
