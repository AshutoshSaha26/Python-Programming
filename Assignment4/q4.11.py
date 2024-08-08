input_string = input("Enter a string: ")
index = int(input("Enter the index to check: "))
char_to_check = input("Enter the character to check for: ")
if 0 <= index < len(input_string):
    if input_string[index] == char_to_check:
        print(f"The character at index {index} is '{char_to_check}'.")
    else:
        print(f"The character at index {index} is not '{char_to_check}'.")
else:
    print("Index is out of range.")
