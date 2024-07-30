def MultiplicationTable(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
n=int(input("Enter any no.:"))
print(f"Multiplication table of {n} is:")
MultiplicationTable(n)