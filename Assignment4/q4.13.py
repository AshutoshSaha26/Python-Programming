import time
def compare_performance(string1, string2):
    start_time = time.time()
    _ = string1 + string2
    concat_time = time.time() - start_time
    start_time = time.time()
    are_equal = string1 == string2
    comparison_time = time.time() - start_time
    start_time = time.time()
    substring_search1 = 'test' in string1
    substring_search2 = 'test' in string2
    substring_search_time = time.time() - start_time
    print(f"Concatenation Time: {concat_time:.6f} seconds")
    print(f"Comparison Time: {comparison_time:.6f} seconds")
    print(f"Substring Search Time in String1: {substring_search_time:.6f} seconds")
    print(f"Substring Search Time in String2: {substring_search_time:.6f} seconds")
    print(f"Are the two strings equal? {are_equal}")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
compare_performance(string1, string2)
