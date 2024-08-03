def count_digits(num):
    return len(str(abs(num)))
number = int(input("Enter an integer: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is: {digit_count}")
