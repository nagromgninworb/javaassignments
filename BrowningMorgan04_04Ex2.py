"""
Author: Morgan Browning
Date: 02/10/2025
Assignment: Module 04 Programming Assignment Part 2

This program sorts a dictionary of items by price and prints the top 3 most expensive items.
"""

def get_items():
    return {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

def get_top_3_items(items):
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:3]

def display_top_3(items):
    print("Top 3 most expensive items:")
    for item, price in items:
        print(f"{item} {price}")

def main():
    items = get_items()
    top_items = get_top_3_items(items)
    display_top_3(top_items)

if __name__ == "__main__":
    main()


