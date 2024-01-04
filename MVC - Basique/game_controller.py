import tkinter as tk
import cv2
import numpy as np

from game_logic import GameLogic
from gesture_detection import GestureDetection
from game_ui import GameUI


class GameController:
    def __init__(self):
        self.current_frame = None
        self.root = tk.Tk()
        self.view = GameUI(self.root, self.playGame)
        self.model = GameLogic()
        self.gestureDetector = GestureDetection()

        self.cap = cv2.VideoCapture(0)
        self.updateCamera()

    def playGame(self):
        playerGesture = np.random.choice(['rock', 'paper', 'scissors'])
        self.model.setPlayerChoice(playerGesture)
        computerGesture = self.model.getComputerChoice()
        winner = self.model.determineWinner()

        self.view.showPlayerGesture(playerGesture)
        self.view.showComputerGesture(computerGesture)
        self.view.showResult(winner)

    def updateCamera(self):
        ret, self.current_frame = self.cap.read()
        if ret:
            self.view.updateCameraFeed(self.current_frame)
        self.root.after(10, self.updateCamera)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = GameController()
    game.run()
