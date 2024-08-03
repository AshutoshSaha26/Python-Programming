def print_alternate_numbers(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=" ")
    print()  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_alternate_numbers(numbers)
