class Employee:
    def __init__(self, emp_id, emp_name, basic_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary
    def calculate_gross_salary(self):
        allowance = 0.20 * self.basic_salary
        gross_salary = self.basic_salary + allowance
        return gross_salary
    def display_info(self):
        gross_salary = self.calculate_gross_salary()
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Gross Salary: {gross_salary}")
if __name__ == "__main__":
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    employee = Employee(emp_id, emp_name, basic_salary)
    employee.display_info()
