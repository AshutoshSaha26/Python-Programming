input_string = input("Enter a sequence of words: ")
words = input_string.split()
digit_words = [word for word in words if word.isdigit()]
print(digit_words)
