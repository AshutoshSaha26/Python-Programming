def reverse_list(input_list):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list
example_list = [1, 2, 3, 4, 5]
print(reverse_list(example_list))  
