def print_multiples_of_10(start, end):
    if start % 10 != 0:
        start += (10 - start % 10)
    for num in range(start, end + 1, 10):
        print(num)
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print_multiples_of_10(start, end)
