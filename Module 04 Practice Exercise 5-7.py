"""

Author: Morgan Browning
Date: 02/09?2025
Assignment: Module 04 Practice Exercise 5-7

This program reads a text file, rxtracts unique words, sorts them in alphabetical order, and displays them.
"""


def get_filename():
    return input("Enter the input file name:")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    
def extract_unique_words(text):
    words=text.split()
    unique_words = sorted(set(words))
    return unique_words

def display_words(word_list):
    for word in word_list:
        print(word)

def main():
    filename = get_filename()
    text = read_file(filename)

    if text: 
        words = extract_unique_words(text)
        display_words(words)

if __name__ == "__main__":
    main()
