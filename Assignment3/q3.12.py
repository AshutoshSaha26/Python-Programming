def print_table(rows):
    for i in range(1, rows + 1):
        print(i, end=" ")
        for j in range(1, 5):
            print(i ** (j - 1), end=" ")
        print()
rows = 5
print_table(rows)
