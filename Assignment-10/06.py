import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 8*x + 15 

np.random.seed(42)
a, b = np.sort(np.random.uniform(-10, 10, 2))

while f(a) * f(b) > 0:
    a, b = np.sort(np.random.uniform(-10, 10, 2))

toler = 1e-6
maxitr = 100
iters = []
roots = []

for i in range(maxitr):
    c = (a + b) / 2.0
    iters.append([a, b, c, f(c)])
    roots.append(c)
    
    if abs(f(c)) < toler:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

iters = np.array(iters)

plt.figure(figsize=(8, 5))
x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x)", color='blue')
plt.axhline(0, color='black', linewidth=1)

plt.scatter(roots, [0]*len(roots), color='red', label="Approximations")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Bisection Method Root Finding")
plt.show()

print(f"Root approximation: {roots[-1]}")