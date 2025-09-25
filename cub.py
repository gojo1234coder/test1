import numpy as np
import matplotlib.pyplot as plt


def cubic_spline(x, y):
    n = len(x) - 1
    h = [x[i+1] - x[i] for i in range(n)]
    alpha = [0] + [(3/h[i])(y[i+1] - y[i]) - (3/h[i-1])(y[i] - y[i-1]) for i in range(1, n)]

    l = [1] + [0]*n
    mu = [0]*n + [0]
    z = [0]*(n+1)

    for i in range(1, n):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1]) / l[i]

    l[n] = 1
    z[n] = 0

    a = y.copy()
    b = [0]*n
    c = [0]*(n+1)
    d = [0]*n

    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = ((a[j+1] - a[j])/h[j]) - h[j](c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j]) / (3*h[j])

    return a, b, c, d


def evaluate(x, a, b, c, d, xp):
    for i in range(len(x) - 1):
        if x[i] <= xp <= x[i+1]:
            dx = xp - x[i]
            return a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
    return None


def plot_spline(x, a, b, c, d, xp, yp):
    x_plot = np.linspace(min(x), max(x), 500)
    y_plot = [evaluate(x, a, b, c, d, xi) for xi in x_plot]

    plt.plot(x, a, 'bo', label='Data Points')
    plt.plot(x_plot, y_plot, 'g-', label='Cubic Spline')
    plt.plot(xp, yp, 'ro', label=f'Interpolated Point ({xp:.2f}, {yp:.2f})')
    plt.title('Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


print("\nCubic Spline Interpolation")
n = int(input("Enter no. of data points: "))
x = []
y = []

print("Enter x and y values:")
for i in range(n):
    xi = float(input(f"  x[{i}]: "))
    yi = float(input(f"  y[{i}]: "))
    x.append(xi)
    y.append(yi)

xp = float(input("Enter x value to interpolate: "))

a, b, c, d = cubic_spline(x, y)
yp = evaluate(x, a, b, c, d, xp)
print(f"\nInterpolated y at x = {xp} is {yp:.4f}")

print("\nSpline Segments:")
for i in range(n - 1):
    print(f"[{x[i]}, {x[i+1]}]: y = {a[i]:.4f} + {b[i]:.4f}(x - {x[i]}) + {c[i]:.4f}(x - {x[i]})² + {d[i]:.4f}(x - {x[i]})³")

plot_spline(x, a, b, c, d, xp, yp)
