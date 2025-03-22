"""
Author: Morgan Browning
Date: 03/03/2025
Assignment: Module 07 Programming Assignment Part 2
"""
class Employee:
    """ Represents an employee with name and employee number. """

    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    def __str__(self):
        return f"Employee Name: {self.name}\nEmployee Number: {self.employee_number}"

class ProductionWorker(Employee):
    """ Represents a production worker, inheriting from Employee. """

    def __init__(self, name, employee_number, hourly_pay_rate, shift_number):
        super().__init__(name, employee_number)
        self.hourly_pay_rate = hourly_pay_rate
        self.shift_number = shift_number  # 1 = Day shift, 2 = Night shift

    def __str__(self):
        shift_type = "Day Shift" if self.shift_number == 1 else "Night Shift"
        return super().__str__() + f"\nHourly Pay Rate: ${self.hourly_pay_rate:.2f}\nShift: {shift_type}"

# Demonstrate functionality
if __name__ == "__main__":
    name = input("Enter employee name: ")
    emp_number = input("Enter employee number: ")
    hourly_rate = float(input("Enter hourly pay rate: "))
    shift = int(input("Enter shift number (1 for Day, 2 for Night): "))

    worker = ProductionWorker(name, emp_number, hourly_rate, shift)

    print("\nEmployee Information:")
    print(worker)
