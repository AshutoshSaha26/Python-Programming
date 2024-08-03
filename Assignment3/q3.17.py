def print_number_pattern(n):
    current_number = 1
    for i in range(1, n + 1):
        for j in range(2 * i - 1):
            print(current_number, end=" ")
            current_number += 1
        print()
n = 3
print_number_pattern(n)
