def SumOfDigits(n):
    sod=0
    while(n>0):
        sod += n%10
        n=n//10
    return sod
n=int(input("Enter a no.:"))
sod=SumOfDigits(n)
print(f"Sum of digits of {n} is {sod}")