"""
Author: Morgan Browning
Date: 02/10/2025
Assignment: Module 04 Practice Exercise 5-8

This program reads a text file and counts the frequency of each unique word. The output displays the words in alphabetical order along with their count.
"""

def get_filename():
    return input("Enter the input file name:")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            return content
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    
import string

def clean_and_split_text(text):
    text = text.lower().strip()
    text = text.translate(str.maketrans("","", string.punctuation))
    words = text.split()
    return words

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word = word.strip()  
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def display_word_frequencies(word_count):
    for word in sorted(word_count.keys()):
        print(word, word_count[word])

def main():
    filename = get_filename()
    text = read_file(filename)

    if text: 
        words = clean_and_split_text(text)
        word_count = count_word_frequency(words)
        display_word_frequencies(word_count)

if __name__ == "__main__":
    main()


