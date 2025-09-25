import sympy as sp
import numpy as np

def get_function():
    expr = input("Enter the function f(x): ")
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(expr), 'numpy')
    return f

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return result

def simpsons_one_third_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requires an even number of intervals.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = (h / 3) * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
    return result

def simpsons_three_eighth_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Simpson's 3/8 rule requires number of intervals divisible by 3.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = (3 * h / 8) * (y[0] + 3 * sum(y[1:-1:3]) + 3 * sum(y[2:-1:3]) + 2 * sum(y[3:-3:3]) + y[-1])
    return result

def main():
    print("Numerical Integration Calculator")
    f = get_function()
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))
    n = int(input("Enter number of subintervals n: "))

    print("\nResults:")
    print(f"Trapezoidal Rule: {trapezoidal_rule(f, a, b, n):.6f}")
    
    try:
        print(f"Simpson's 1/3 Rule: {simpsons_one_third_rule(f, a, b, n):.6f}")
    except ValueError as e:
        print(f"Simpson's 1/3 Rule: Error - {e}")
    
    try:
        print(f"Simpson's 3/8 Rule: {simpsons_three_eighth_rule(f, a, b, n):.6f}")
    except ValueError as e:
        print(f"Simpson's 3/8 Rule: Error - {e}")

if __name__ == "__main__":
    main()
