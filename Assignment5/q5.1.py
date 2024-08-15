ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
ages.extend([min_age, max_age])
median_age = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
average_age = sum(ages) / len(ages)
age_range = max_age - min_age
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Range of ages:", age_range)
print("Difference between min age and average:", min_diff)
print("Difference between max age and average:", max_diff)
