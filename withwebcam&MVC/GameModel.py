import random


class GameModel:
    def __init__(self):
        self.scores = [0, 0]  # Scores [IA, Joueur]
        self.playerMove = None
        self.aiMove = None

    def update_player_move(self, move):
        """
        Met à jour le mouvement du joueur.
        """
        self.playerMove = move

    def generate_ai_move(self):
        """
        Génère un mouvement aléatoire pour l'IA.
        """
        self.aiMove = random.randint(1, 3)

    def update_scores(self):
        """
        Met à jour les scores en fonction des mouvements du joueur et de l'IA.
        """
        if self.playerMove is not None and self.aiMove is not None:
            # Logique pour déterminer le gagnant et mettre à jour les scores
            if (self.playerMove == 1 and self.aiMove == 3) or \
                    (self.playerMove == 2 and self.aiMove == 1) or \
                    (self.playerMove == 3 and self.aiMove == 2):
                self.scores[1] += 1  # Joueur gagne

            elif (self.playerMove == 3 and self.aiMove == 1) or \
                    (self.playerMove == 1 and self.aiMove == 2) or \
                    (self.playerMove == 2 and self.aiMove == 3):
                self.scores[0] += 1  # IA gagne
            # Réinitialiser les mouvements après la mise à jour des scores
            self.playerMove = None
            self.aiMove = None

    def get_scores(self):
        """
        Retourne les scores actuels.
        """
        return self.scores
