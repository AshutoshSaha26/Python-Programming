from collections import Counter
input_string = input("Enter a string: ")
words = input_string.split()
word_count = Counter(words)
print("Word counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")
