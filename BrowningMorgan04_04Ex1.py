"""
Author: Morgan Browning
Date: 02/10/2025
Assignment: Module 04 Programming Assignment Part 1

This program asks the user for a number greater than 1, then finds all prime numbers up to that number.
It uses a function to check if a number is prime and prints all primes.
"""

def get_number():
    return int(input("Enter an integer greater than 1: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def display_primes(primes):
    print("Prime numbers up to the entered value:")
    for prime in primes:
        print(prime)

def main():
    number = get_number()
    primes = find_primes(number)
    display_primes(primes)

if __name__ == "__main__":
    main()
