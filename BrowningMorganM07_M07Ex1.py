"""
Author: Morgan Browning
Date: 03/03/2025
Assignment: Module 07 Programming Assignment Part 1
"""

class Person:
    """ Represents a person with name, address, and telephone. """
    
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone: {self.telephone}"

class Customer(Person):
    """ Represents a customer, inheriting from Person. """

    def __init__(self, name, address, telephone, customer_number, mailing_list):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list  # True or False

    def __str__(self):
        mailing_status = "Yes" if self.mailing_list else "No"
        return super().__str__() + f"\nCustomer Number: {self.customer_number}\nMailing List: {mailing_status}"

# Demonstrate functionality
if __name__ == "__main__":
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    phone = input("Enter customer phone: ")
    customer_number = input("Enter customer number: ")
    mailing_list = input("Join mailing list? (yes/no): ").strip().lower() == "yes"

    customer = Customer(name, address, phone, customer_number, mailing_list)
    
    print("\nCustomer Information:")
    print(customer)
