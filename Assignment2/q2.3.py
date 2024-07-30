def gcd(a,b):
    while b:
        a,b=b,(a%b)
    return a
a=int (input("Enter 1st no."))
b=int (input("Enter 2nd no."))
r=gcd(a,b)
print(f"GCD of {a} and {b} is {r}")