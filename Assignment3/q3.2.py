def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Undefined (vertical line)'
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope
print(calculate_slope(1, 2, 3, 4))  
print(calculate_slope(1, 2, 1, 5))  
print(calculate_slope(0, 0, 4, 2))  