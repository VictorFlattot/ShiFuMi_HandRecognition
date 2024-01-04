import cv2
import time
from HandDetectorFiles import HandDetector
from GameModel import GameModel  # Assurez-vous d'avoir implémenté GameModel
from GameView import GameView  # Assurez-vous d'avoir implémenté GameView


def interpret_player_move(fingers):
    """
    Interprète le mouvement du joueur en fonction des doigts levés.
    """
    if fingers == [0, 0, 0, 0, 0]:
        return 1  # Pierre
    elif fingers == [1, 1, 1, 1, 1]:
        return 2  # Papier
    elif fingers == [0, 1, 1, 0, 0]:
        return 3  # Ciseaux
    else:
        return None  # Mouvement non reconnu ou aucun mouvement


class GameController:
    def __init__(self):
        self.model = GameModel()
        self.view = GameView("Resources/Background.png", "Resources")
        self.detector = HandDetector(maxHands=1)
        self.startGame = False
        self.stateResult = False
        self.timer = 0
        self.initialTime = 0
        self.delayBetweenRounds = 5  # Délai en secondes
        self.nextRoundTime = 0  # Moment où la prochaine manche doit commencer
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

    def run(self):
        while True:
            # Réinitialiser l'image de fond

            success, img = self.cap.read()
            if not success:
                break

            img = cv2.flip(img, 1)
            imgScaled = cv2.resize(img, (0, 0), None, 1, 0.63)
            imgScaled = imgScaled[0:640, 0:480]

            hands, img = self.detector.findHands(imgScaled)  # avec dessin

            currentTime = time.time()

            if time.time() < self.nextRoundTime:
                self.initialTime = time.time()

            if self.startGame \
                    and (self.model.scores[0] <= 4 and self.model.scores[1] <= 4) \
                    and time.time() > self.nextRoundTime:
                self.view.reset_background("Resources/Background.png")

                if not self.stateResult:
                    # Mise à jour et affichage du timer
                    self.timer = currentTime - self.initialTime
                    self.view.show_timer(self.timer)

                if self.timer > 3:
                    self.stateResult = True

                    if hands:
                        hand = hands[0]
                        fingers = self.detector.fingersUp(hand)
                        playerMove = interpret_player_move(fingers)
                        self.model.update_player_move(playerMove)

                        self.model.generate_ai_move()
                        self.view.show_game_result(self.stateResult, self.model.aiMove)
                        self.model.update_scores()

                    self.nextRoundTime = time.time() + self.delayBetweenRounds
            else:
                # Réinitialisation pour le prochain tour
                self.stateResult = False

            self.view.update_background(imgScaled)
            self.view.display_scores(self.model.get_scores())

            key = cv2.waitKey(1)
            if key == ord('s') and not self.startGame:
                self.start_game()
                self.initialTime = time.time()
                self.stateResult = False
            elif key == ord('q'):
                break

            self.view.show()

        self.cap.release()
        cv2.destroyAllWindows()

    def start_game(self):
        self.startGame = True
        self.initialTime = time.time()
        self.stateResult = False
        self.nextRoundTime = 0  # Commence immédiatement la première manche



if __name__ == "__main__":
    controller = GameController()
    controller.run()
