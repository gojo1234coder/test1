import sympy as sp
import math

def euler_method_sympy(f_expr, x0, y0, x_end, h):
    x_sym, y_sym = sp.symbols('x y')
    f = sp.lambdify((x_sym, y_sym), f_expr)
    x = x0
    y = y0
    while x < x_end:
        y += h * f(x, y)
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

y_final = euler_method_sympy(f_expr, x0, y0, x_end, h)

print(f"\nApproximate solution at x = {x_end}: y ≈ {y_final:.5f}")

