student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}
length_of_student_dict = len(student)
skills_value = student['skills']
skills_type = type(skills_value)
student['skills'].extend(['Machine Learning', 'Web Development'])
keys_list = list(student.keys())
values_list = list(student.values())
items_list = list(student.items())
del student['address']
del student
print("Length of student dictionary:", length_of_student_dict)
print("Skills value:", skills_value)
print("Skills data type:", skills_type)
print("Keys list:", keys_list)
print("Values list:", values_list)
print("Items list:", items_list)
try:
    print(student)  
except NameError:
    print("The student dictionary has been deleted.")
