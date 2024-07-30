def fibonacci_series(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)   
    return fib_series[:n]
num_terms = int(input("Enter the number of terms: "))
series = fibonacci_series(num_terms)
print(f"The first {num_terms} terms of the Fibonacci series are:")
for term in series:
    print(term)
