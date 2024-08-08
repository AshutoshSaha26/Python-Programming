string = input("Enter a string: ")
string_length = len(string)
print(f"Length of the string: {string_length}")
substring = "country"
if substring in string:
    print(f"The substring '{substring}' was found in the string.")
else:
    print(f"The substring '{substring}' was not found in the string.")
word_count = {}
words = string.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Occurrences of each word:")
for word, count in word_count.items():
    print(f"{word}: {count}")
