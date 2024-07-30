def factorial_series(n):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    series = []
    for i in range(1, n + 1):
        series.append(factorial(i))
    
    return series
num_terms = int(input("Enter the number of terms: "))
series = factorial_series(num_terms)
print(f"The first {num_terms} terms of the series are:")
for term in series:
    print(term)
