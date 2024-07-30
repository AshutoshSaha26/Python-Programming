import math
def sqrt(n1,n2,n3):
    if (n1<0 or n2<0 or n3<0):
        return "Square root of negative nos is not defined"
    else:

        sq1=math.sqrt(n1)
        sq2=math.sqrt(n2)
        sq3=math.sqrt(n3)
        return sq1,sq2,sq3
n1=int(input("Enter no1:"))    
n2=int(input("Enter no2:"))
n3=int(input("Enter no3:"))  
r1,r2,r3=(sqrt(n1,n2,n3))
print("Square root of: No1 is ", r1, " No2 is ", r2, " No3 is ",r3)
