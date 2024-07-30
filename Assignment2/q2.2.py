import math
def solve_quadratic(a,b,c):
    if a==0:
        return "Coeffeient 'a' cannot be 0"
    discriminant=b**2 - 4*a*c
    if (discriminant<0):
        return "Equation has no real roots"
    root1= (-b + math.sqrt(discriminant))/(2*a)
    root2= (-b - math.sqrt(discriminant))/(2*a)
    return root1, root2
a=int(input("Enter valur for a:"))
b=int(input("Enter valur for b:"))
c=int(input("Enter valur for c:"))
s1,s2=(solve_quadratic(a,b,c))
print(f"Solutions for equation {a}x^2 + {b}x + {c} are {s1} and {s2}")