import cmath
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)   
    return root1, root2
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
root1, root2 = find_roots(a, b, c)
print(f"The roots of the quadratic equation {a}x^2 + {b}x + {c} = 0 are:")
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
