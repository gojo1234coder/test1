import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def newton_forward(x_vals, y_vals):
    n = len(x_vals)
    x = sp.symbols('x')

    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_vals
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i+1][j-1] - diff_table[i][j-1]

    print("\nForward Difference Table:")
    print(diff_table)

    h = x_vals[1] - x_vals[0]
    p = (x - x_vals[0]) / h
    P = y_vals[0]
    term = 1
    for j in range(1, n):
        term *= (p - (j-1)) / j
        P += diff_table[0][j] * term

    return sp.simplify(P.expand())


def newton_backward(x_vals, y_vals):
    n = len(x_vals)
    x = sp.symbols('x')

    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_vals
    for j in range(1, n):
        for i in range(j, n):
            diff_table[i][j] = diff_table[i][j-1] - diff_table[i-1][j-1]

    print("\nBackward Difference Table:")
    print(diff_table)

    h = x_vals[1] - x_vals[0]
    p = (x - x_vals[-1]) / h
    P = y_vals[-1]
    term = 1
    for j in range(1, n):
        term *= (p + (j-1)) / j
        P += diff_table[-1][j] * term

    return sp.simplify(P.expand())


def interpolate_and_plot(x_vals, y_vals, query_points, deriv_points):
    x = sp.symbols('x')

    P_forward = newton_forward(x_vals, y_vals)
    P_backward = newton_backward(x_vals, y_vals)

    print("\nForward Polynomial P_f(x):")
    print(P_forward)
    print("\nBackward Polynomial P_b(x):")
    print(P_backward)

    P1_f, P2_f = sp.diff(P_forward, x), sp.diff(P_forward, x, 2)
    P1_b, P2_b = sp.diff(P_backward, x), sp.diff(P_backward, x, 2)

    print("\nForward First Derivative:")
    print(P1_f)
    print("\nForward Second Derivative:")
    print(P2_f)

    print("\nBackward First Derivative:")
    print(P1_b)
    print("\nBackward Second Derivative:")
    print(P2_b)

    print("\nResults:")
    for qp in query_points:
        print(f"Forward f({qp}) = {float(P_forward.subs(x, qp))}")
        print(f"Backward f({qp}) = {float(P_backward.subs(x, qp))}")

    for dp in deriv_points:
        print(f"Forward f'({dp}) = {float(P1_f.subs(x, dp))}, f''({dp}) = {float(P2_f.subs(x, dp))}")
        print(f"Backward f'({dp}) = {float(P1_b.subs(x, dp))}, f''({dp}) = {float(P2_b.subs(x, dp))}")

    X = np.linspace(min(x_vals)-0.2, max(x_vals)+0.2, 200)
    Yf = [float(P_forward.subs(x, xx)) for xx in X]
    Yb = [float(P_backward.subs(x, xx)) for xx in X]

    plt.figure(figsize=(10,6))
    plt.plot(X, Yf, label="Forward P(x)")
    plt.plot(X, Yb, label="Backward P(x)", linestyle="dashed")
    plt.scatter(x_vals, y_vals, color="red", label="Data Points")
    plt.legend()
    plt.grid(True)
    plt.title("Newton Forward & Backward Interpolation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()


def get_input_list(prompt):
    return list(map(float, input(prompt).strip().split()))

print("Newton's Interpolation with Derivatives")
n = int(input("Enter number of data points: "))

x_vals = []
y_vals = []
print(f"Enter {n} values for x and y (space-separated on each line):")
for i in range(n):
    x, y = map(float, input(f"Point {i+1}: ").strip().split())
    x_vals.append(x)
    y_vals.append(y)

query_points = get_input_list("Enter the x values to interpolate (space-separated): ")
deriv_points = get_input_list("Enter the x values to evaluate derivatives (space-separated): ")

interpolate_and_plot(x_vals, y_vals, query_points, deriv_points)