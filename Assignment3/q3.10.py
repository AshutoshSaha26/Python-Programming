def get_digit_segments(digit):
    # Define the segments for each digit
    segments = {
        0: (" _ ", "| |", "|_|"),
        1: ("   ", "  |", "  |"),
        2: (" _ ", " _|", "|_ "),
        3: (" _ ", " _|", " _|"),
        4: ("   ", "|_|", "  |"),
        5: (" _ ", "|_ ", " _|"),
        6: (" _ ", "|_ ", "|_|"),
        7: (" _ ", "  |", "  |"),
        8: (" _ ", "|_|", "|_|"),
        9: (" _ ", "|_|", " _|")
    }
    return segments[digit]
def print_number_as_segment_display(N):
    number_str = str(N)
    lines = ["", "", ""]  
    for digit_char in number_str:
        digit = int(digit_char)
        digit_lines = get_digit_segments(digit)     
        for i in range(3):
            lines[i] += digit_lines[i] + " " 
    for line in lines:
        print(line)
N = int(input("Enter the number N: "))
print_number_as_segment_display(N)
