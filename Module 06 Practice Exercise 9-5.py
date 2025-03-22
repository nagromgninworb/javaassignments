"""
Author: Morgan 
Date: 02/22/2024
Assignment: Module 06 Practice Exercise 9-5

This program creates a GUI-based number guessing game using the breezypythongui library.
The computer generates a random number between 1 and 100, and the user provides hints
using buttons labeled 'Too Small', 'Too Large', or 'Correct'. The game continues until 
the correct number is guessed, after which the buttons are disabled, and a 'New Game' 
button appears to restart the game.
"""

# Import necessary libraries
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages")

from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    """GUI-based guessing game where the computer guesses a number between 1 and 100"""

    def __init__(self):
        """Initialize the GUI frame and game variables"""
        EasyFrame.__init__(self, title="Guess the Number", width=300, height=200)

        # Initialize game state
        self.low = 1
        self.high = 100
        self.computer_guess = random.randint(self.low, self.high)  # First guess

        # Add GUI components
        self.addLabel("Computer's Guess:", row=0, column=0)
        self.guessLabel = self.addLabel(str(self.computer_guess), row=0, column=1)  # Display the first guess

        # Add buttons for user hints
        self.tooSmallBtn = self.addButton("Too Small", row=1, column=0, command=self.tooSmall)
        self.tooLargeBtn = self.addButton("Too Large", row=1, column=1, command=self.tooLarge)
        self.correctBtn = self.addButton("Correct", row=2, column=0, command=self.correct)

        # New Game Button (Initially disabled)
        self.newGameBtn = self.addButton("New Game", row=2, column=1, command=self.newGame, state="disabled")

    def tooSmall(self):
        """Handles the 'Too Small' button press"""
        self.low = self.computer_guess + 1
        self.updateGuess()

    def tooLarge(self):
        """Handles the 'Too Large' button press"""
        self.high = self.computer_guess - 1
        self.updateGuess()

    def correct(self):
        """Handles the 'Correct' button press"""
        self.messageBox("Congratulations!", "The computer guessed correctly!")
        self.disableGame()

    def updateGuess(self):
        """Updates the computer's guess and refreshes the GUI"""
        if self.low <= self.high:
            self.computer_guess = random.randint(self.low, self.high)
            self.guessLabel["text"] = str(self.computer_guess)  # Update label
            self.update()  # Force GUI refresh
        else:
            self.messageBox("Game Over", "Something went wrong. Starting a new game.")
            self.newGame()

    def disableGame(self):
        """Disables the guess buttons and enables the new game button"""
        self.tooSmallBtn["state"] = "disabled"
        self.tooLargeBtn["state"] = "disabled"
        self.correctBtn["state"] = "disabled"
        self.newGameBtn["state"] = "normal"

    def newGame(self):
        """Resets the game state and enables the buttons for a new round"""
        self.low = 1
        self.high = 100
        self.computer_guess = random.randint(self.low, self.high)
        self.guessLabel["text"] = str(self.computer_guess)  # Show new guess
        self.update()  # Force GUI refresh

        # Enable buttons
        self.tooSmallBtn["state"] = "normal"
        self.tooLargeBtn["state"] = "normal"
        self.correctBtn["state"] = "normal"
        self.newGameBtn["state"] = "disabled"

# Run the GUI Application
if __name__ == "__main__":
    GuessingGame().mainloop()
