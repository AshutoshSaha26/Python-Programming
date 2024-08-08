lines = []
print("Enter a sequence of lines (type 'END' to stop):")
while True:
    line = input()
    if line == 'END':
        break
    lines.append(line)
capitalized_lines = [line.upper() for line in lines]
print("\nOutput:")
for line in capitalized_lines:
    print(line)
