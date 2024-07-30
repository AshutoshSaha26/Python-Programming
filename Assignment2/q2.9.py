def DecToBin(d):
    if d==0:
        return 0
    b=""
    while(d>0):
        b=str(d%2)+b
        d=d//2
    return b
d=int(input("Enter decimal:"))
b=DecToBin(d)
print(f"Dec {d} to Bin is {b}")
