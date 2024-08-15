class Complex:
    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary
    def add(self, other):
        real_sum = self.__real + other.__real
        imaginary_sum = self.__imaginary + other.__imaginary
        print(f"Added Complex Number: {real_sum} + {imaginary_sum}i")
if __name__ == "__main__":
    complex1 = Complex(3, 2)  
    complex2 = Complex(1, 7)  
    complex1.add(complex2)
