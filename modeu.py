import sympy as sp
import math

def modified_euler_method(f_expr, x0, y0, x_end, h):
    x_sym, y_sym = sp.symbols('x y')
    f = sp.lambdify((x_sym, y_sym), f_expr, modules=["math"])
    x = x0
    y = y0
    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += (h / 2) * (k1 + k2)
        x += h
    return y

print("Enter the differential equation dy/dx = f(x, y)")
user_input = input("f(x, y) = ")

x_sym, y_sym = sp.symbols('x y')
f_expr = sp.sympify(user_input)

x0 = float(input("Initial x (x0): "))
y0 = float(input("Initial y (y0): "))
x_end = float(input("Target x : "))
h = float(input("Step size h : "))

y_final = modified_euler_method(f_expr, x0, y0, x_end, h)

print(f"\nApproximate solution at x = {x_end}: y ≈ {y_final:.5f}")
