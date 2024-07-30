import math
def isKrishnamurthy(n):
    digits=str(n)
    sof=0
    for i in digits:
        sof += math.factorial(int(i))
    return sof == n
n=int(input("Enter any no. :"))
if isKrishnamurthy(n):
    print("Krishnamurthy no.")
else:
    print("Not a Krishnamurthy no.")