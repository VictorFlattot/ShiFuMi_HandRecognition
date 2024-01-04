import cv2
from Utility import overlayPNG

class GameView:
    def __init__(self, background_path, resource_path):
        self.imgBG = cv2.imread(background_path)
        self.resource_path = resource_path

    def update_background(self, imgScaled):
        """
        Met à jour l'image de fond avec l'image de la webcam.
        """
        region_height = imgScaled.shape[0]
        bottom_position = 340  # Déplacer vers le bas de 5 pixels
        right_position = 769   # Déplacer vers la droite de 10 pixels
        self.imgBG[bottom_position:bottom_position + region_height, right_position:right_position + imgScaled.shape[1]] = imgScaled

    def display_scores(self, scores):
        """
        Affiche les scores sur l'écran.
        """
        cv2.putText(self.imgBG, str(scores[0]), (410, 250), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 127), 6)
        cv2.putText(self.imgBG, str(scores[1]), (1151, 250), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 127), 6)

    def show_game_result(self, stateResult, aiMove):
        """
        Affiche l'état actuel du jeu, y compris le résultat et l'image de l'IA.
        """
        if stateResult:
            print (aiMove)
            imgAI = cv2.imread(f'{self.resource_path}/{aiMove}.png', cv2.IMREAD_UNCHANGED)
            overlayPNG(self.imgBG, imgAI, (149, 340))

    def show_timer(self, timer):
        """
        Affiche le timer sur l'écran.
        """
        cv2.putText(self.imgBG, str(int(timer)), (607, 460), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 6)

    def show(self):
        """
        Affiche l'image finale dans la fenêtre de l'application.
        """
        cv2.imshow("Game", self.imgBG)

    def reset_background(self, original_background_path):
        """
        Réinitialise l'image de fond à son état original.
        """
        self.imgBG = cv2.imread(original_background_path)