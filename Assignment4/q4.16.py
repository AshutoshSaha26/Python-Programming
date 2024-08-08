input_string = input("Enter a string: ")
words = input_string.split()
seen_words = set()
unique_words = []
for word in words:
    if word not in seen_words:
        unique_words.append(word)
        seen_words.add(word)
result_string = ' '.join(unique_words)
print(f"String with repeated words removed: {result_string}")
