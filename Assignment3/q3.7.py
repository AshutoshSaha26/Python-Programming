import math
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
def compute_sin(x, n):
    sin_x = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_x += term
    return sin_x
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))
result = compute_sin(x, n)
print(f"The computed value of sin({x}) using {n} terms is: {result}")
print(f"The value of sin({x}) using math.sin is: {math.sin(x)}")
