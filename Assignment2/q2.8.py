def PowerRecursion(b,e):
    if e==0:
        return 1
    else:
        return b * PowerRecursion(b, e-1) 
b=int(input("Enter base value:"))   
e=int(input("Enter exponent value:"))     
r=PowerRecursion(b,e)
print(f"{b} to the power of {e} is {r}")
