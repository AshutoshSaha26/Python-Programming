def PrintNumberInWord(number):
    number_to_word = {
        0: "ZERO",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE"
    }
    if number in number_to_word:
        print(number_to_word[number])
    else:
        print("Number not in range")
if __name__ == "__main__":
    try:
        number = int(input("Enter an integer between 0 and 9: "))
        PrintNumberInWord(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")
