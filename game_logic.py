import numpy as np


class GameLogic:
    def __init__(self):
        self.playerChoice = None
        self.computerChoice = None

    def setPlayerChoice(self, choice):
        self.playerChoice = choice

    def getComputerChoice(self):
        self.computerChoice = np.random.choice(['rock', 'paper', 'scissors'])
        return self.computerChoice

    def determineWinner(self):
        if self.playerChoice == self.computerChoice:
            return "Draw!"
        if (
                (self.playerChoice == "rock" and self.computerChoice == "scissors") or
                (self.playerChoice == "scissors" and self.computerChoice == "paper") or
                (self.playerChoice == "paper" and self.computerChoice == "rock")
        ):
            return "Player wins!"
        else:
            return "Computer wins!"

