def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) * 2, end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        for j in range(2, i + 1):
            print(j, end=" ")
        print()
n = 4
print_pattern(n)
