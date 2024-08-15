class Student:
    def __init__(self, name, roll_no, sub1, sub2):
        self.name = name
        self.roll_no = roll_no
        self.sub1 = sub1
        self.sub2 = sub2
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Subject 1 Marks: {self.sub1}")
        print(f"Subject 2 Marks: {self.sub2}")
    def total_marks(self):
        return self.sub1 + self.sub2
    def percentage(self):
        total = self.total_marks()
        return (total / 200) * 100  
if __name__ == "__main__":
    student = Student("John Doe", "12345", 85, 90)
    student.display_info()
    print(f"Total Marks: {student.total_marks()}")
    print(f"Percentage: {student.percentage()}%")
