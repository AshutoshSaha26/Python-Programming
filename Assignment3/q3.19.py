def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (i - 1), end="")
        print(i, end="")
        if i != n:
            print(" " * (2 * (n - i) - 1), end="")
            print(i)
        else:
            print()
n = 4
print_pattern(n)
