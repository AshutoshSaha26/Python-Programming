input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
print(f"Reversed String: {reversed_string}")
is_palindrome = input_string == reversed_string
print(f"Is Palindrome: {is_palindrome}")
substring = input("Enter the substring to check: ")
ends_with_substring = input_string.endswith(substring)
print(f"Ends with '{substring}': {ends_with_substring}")
capitalized_string = input_string.title()
print(f"Capitalized String: {capitalized_string}")
another_string = input("Enter another string to check for anagram: ")
is_anagram = sorted(input_string.replace(" ", "").lower()) == sorted(another_string.replace(" ", "").lower())
print(f"Is Anagram: {is_anagram}")
vowels = "aeiouAEIOU"
string_without_vowels = ''.join([char for char in input_string if char not in vowels])
print(f"String without vowels: {string_without_vowels}")
words = input_string.split()
longest_word_length = max(len(word) for word in words)
print(f"Length of the longest word: {longest_word_length}")
