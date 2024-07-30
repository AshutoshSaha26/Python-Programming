def geometric_sequence(first_term, common_ratio, num_terms):
    sequence = []
    term = first_term
    for _ in range(num_terms):
        sequence.append(term)
        term *= common_ratio
    return sequence
first_term = 2
common_ratio = 3
num_terms = 6
sequence = geometric_sequence(first_term, common_ratio, num_terms)
print("The first 6 terms of the geometric sequence are:")
for term in sequence:
    print(term)
