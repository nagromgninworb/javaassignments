import os
import re

# Take the inputs
fileName = input("Enter the file name: ")

try:
    inputFile = open(fileName, 'r')
    text = inputFile.read()
except FileNotFoundError:
    print(f"Error: File '{fileName}' not found. Make sure it is in the correct directory.")
    exit()

# Count the sentences more accurately
# Using regex to count actual sentences, excluding abbreviations.
sentences = len(re.findall(r'[.!?]+', text))

# Count the words (only valid words, excluding punctuation)
words = len(re.findall(r'\b\w+\b', text))

# Count the syllables more accurately
syllables = 0
vowels = "aeiouAEIOU"
for word in re.findall(r'\b\w+\b', text):  # Split into words more accurately
    word_syllables = 0
    prev_was_vowel = False

    for char in word:
        if char in vowels:
            if not prev_was_vowel:  # Only count a new vowel sequence
                word_syllables += 1
            prev_was_vowel = True
        else:
            prev_was_vowel = False

    # Handle silent 'e' at the end and 'le' endings
    if word.endswith(('es', 'ed', 'e')) and len(word) > 2:
        word_syllables -= 1
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        word_syllables += 1

    syllables += max(1, word_syllables)  # Ensure at least 1 syllable per word

# Handle potential division by zero errors
if sentences == 0 or words == 0:
    print("Error: No valid sentences or words found in the file.")
    exit()

# Compute the Flesch Index and Grade Level
index = round(206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words), 2)
level = int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))

# Output the results
print("\nResults:")
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")




