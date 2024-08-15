class ThreeDigitNumber:
    def __init__(self, num):
        if 100 <= num <= 999:  
            self.__num = num
        else:
            raise ValueError("Number must be a 3-digit number.")
    def display_reverse(self):
        reversed_num = int(str(self.__num)[::-1])
        print(f"Original Number: {self.__num}")
        print(f"Reversed Number: {reversed_num}")
if __name__ == "__main__":
    try:
        number = ThreeDigitNumber(321)
        number.display_reverse()
    except ValueError as e:
        print(e)
