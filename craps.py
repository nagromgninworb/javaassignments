"""
File: craps.py

This module studies and plays the game of craps.
"""

from die import Die

class Player:
    """ Represents a player in the game of craps. """

    def __init__(self):
        """ Initializes player attributes. """
        self.die1 = Die()  # First die object
        self.die2 = Die()  # Second die object
        self.rollsCount = 0  # Number of rolls made
        self.atStartup = True  # Tracks if first roll has happened
        self.winner = False  # Boolean flag for winner
        self.loser = False  # Boolean flag for loser
        self.roll = (0, 0)  # Stores the last roll

    def rollDice(self):
        """ Rolls two dice, updates roll count, and returns the values. """
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        self.roll = (self.die1.getValue(), self.die2.getValue())  # Store roll
        self.rollsCount += 1
        return self.roll  # Returns a tuple of dice values

    def getNumberOfRolls(self):
        """ Returns the total number of rolls made. """
        return self.rollsCount

    def isWinner(self):
        """ Determines if the player has won. """
        total = sum(self.roll)
        if self.atStartup and total in (7, 11):
            self.winner = True
        return self.winner

    def isLoser(self):
        """ Determines if the player has lost. """
        total = sum(self.roll)
        if self.atStartup and total in (2, 3, 12):
            self.loser = True
        return self.loser

def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    print("Rolling dice...")
    
    while not player.isWinner() and not player.isLoser():
        roll_result = player.rollDice()
        print(f"Roll: {roll_result}, Total: {sum(roll_result)}")
    
    if player.isWinner():
        print("You win!")
    elif player.isLoser():
        print("You lose!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    for _ in range(number):
        player = Player()
        while not player.isWinner() and not player.isLoser():
            player.rollDice()
        if player.isWinner():
            wins += 1
            winRolls += player.getNumberOfRolls()
        else:
            losses += 1
            lossRolls += player.getNumberOfRolls()
    
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    if wins > 0:
        print("The average number of rolls per win is %0.2f" % (winRolls / wins))
    if losses > 0:
        print("The average number of rolls per loss is %0.2f" % (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()
