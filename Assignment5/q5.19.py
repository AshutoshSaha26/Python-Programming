class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    def display(self):
        return f"{self.empid}\t{self.name}\t{self.salary:.2f}"
if __name__ == "__main__":
    employees = []
    for i in range(5):
        empid = input(f"Enter Employee ID for employee {i + 1}: ")
        name = input(f"Enter Employee Name for employee {i + 1}: ")
        salary = float(input(f"Enter Employee Salary for employee {i + 1}: "))
        employees.append(Employee(empid, name, salary))
    print(f"{'Emp ID':<10}{'Name':<20}{'Salary':<10}")
    print("-" * 40)
    for employee in employees:
        print(employee.display())
