import tkinter as tk
from tkinter import Label, Button


class GameUI:
    def __init__(self, master, play_callback):
        self.playButton = None
        self.resultLabel = None
        self.gestureLabel = None
        self.computerGestureLabel = None
        self.cameraDisplay = None
        self.play_callback = play_callback
        self.window = master
        self.initializeUI()

    def initializeUI(self):
        self.playButton = Button(self.window, text="Play", command=self.promptForPlay)
        self.playButton.pack()

        self.resultLabel = Label(self.window, text="")
        self.resultLabel.pack()

        self.gestureLabel = Label(self.window, text="")
        self.gestureLabel.pack()

        self.computerGestureLabel = Label(self.window, text="")
        self.computerGestureLabel.pack()

        self.cameraDisplay = Label(self.window)
        self.cameraDisplay.pack()

    def showResult(self, result):
        self.resultLabel.config(text=result)

    def promptForPlay(self):
        self.play_callback()

    def showPlayerGesture(self, gesture):
        self.gestureLabel.config(text=f"Your Choice: {gesture}")

    def showComputerGesture(self, gesture):
        self.computerGestureLabel.config(text=f"Computer's Choice: {gesture}")

    def updateCameraFeed(self, frame):
        pass
