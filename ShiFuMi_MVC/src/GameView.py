import cv2
from Utility import overlayPNG

class GameView:
    def __init__(self, background_path, resource_path):
        """
        Initialise une nouvelle instance de GameView.

        Args:
            background_path (str): Chemin d'accès à l'image de fond utilisée dans le jeu.
            resource_path (str): Chemin d'accès au dossier contenant les ressources du jeu (comme les images).
        """
        self.imgBG = cv2.imread(background_path)
        self.resource_path = resource_path

    def update_background(self, imgScaled):
        """
        Met à jour l'image de fond avec l'image de la webcam.

        Args:
            imgScaled (numpy.ndarray): Image capturée par la webcam, redimensionnée pour correspondre à la taille requise.
        """
        region_height = imgScaled.shape[0]
        bottom_position = 340
        right_position = 769
        self.imgBG[bottom_position:bottom_position + region_height, right_position:right_position + imgScaled.shape[1]] = imgScaled

    def display_scores(self, scores):
        """
        Affiche les scores des joueurs sur l'image de fond.

        Args:
            scores (list): Liste contenant les scores des joueurs [score IA, score joueur].
        """
        cv2.putText(self.imgBG, str(scores[0]), (410, 250), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 127), 6)
        cv2.putText(self.imgBG, str(scores[1]), (1151, 250), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 127), 6)

    def show_game_result(self, stateResult, aiMove):
        """
        Affiche le résultat du jeu et l'image correspondante à l'action de l'IA.

        Args:
            stateResult (bool): État indiquant si le résultat doit être affiché.
            aiMove (int): Le mouvement de l'IA, utilisé pour sélectionner l'image correspondante.
        """
        if stateResult:
            imgAI = cv2.imread(f'../{self.resource_path}/{aiMove}.png', cv2.IMREAD_UNCHANGED)
            overlayPNG(self.imgBG, imgAI, (149, 340))

    def display_winner(self, scores):
        if scores[0] == 5 or scores[1] == 5:
            winner_text = "Player" if scores[1] == 5 else "Computer"
            cv2.putText(self.imgBG, 'Winner is', (570, 425), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 5)
            cv2.putText(self.imgBG, winner_text, (571, 462), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 5)

            # Charger et superposer l'image de confettis
            confetti_img = cv2.imread(f'../{self.resource_path}/winner.png', cv2.IMREAD_UNCHANGED)
            confetti_position = (250, 145) if winner_text == "Computer" else (969, 145)
            self.imgBG = overlayPNG(self.imgBG, confetti_img, confetti_position)

    def show_timer(self, timer):
        """
        Affiche un compte à rebours sur l'écran.

        Args:
            timer (int): Valeur du timer à afficher.
        """
        cv2.putText(self.imgBG, str(int(timer)), (607, 460), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 6)

    def show(self):
        """
        Affiche l'image de fond actuelle dans une fenêtre nommée 'Game'.
        """
        cv2.imshow("Game", self.imgBG)

    def reset_background(self, original_background_path):
        """
        Réinitialise l'image de fond à son état original.

        Args:
            original_background_path (str): Chemin d'accès à l'image de fond originale.
        """
        self.imgBG = cv2.imread(original_background_path)
