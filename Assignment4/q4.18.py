string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
all_chars_present = all(char in string2 for char in string1)
if all_chars_present:
    print("All characters in the first string are present in the second string.")
else:
    print("Not all characters in the first string are present in the second string.")
