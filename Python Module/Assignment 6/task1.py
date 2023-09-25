import json


class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state


def read_employee_data():
    with open('employee.json', 'r') as file:
        data = json.load(file)
        employees = []
        for employee_info in data:
            employees.append(Employee(
                employee_info['Name'],
                employee_info['DOB'],
                employee_info['Height'],
                employee_info['City'],
                employee_info['State']
            ))
        return employees



employees = read_employee_data()
for employee in employees:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")
