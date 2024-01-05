import random

class GameModel:
    def __init__(self):
        """
        Initialise une nouvelle instance de GameModel.
        Initialise les scores pour l'IA et le joueur à 0 et définit les mouvements du joueur et de l'IA à None.
        """
        self.scores = [0, 0]  # Scores [IA, Joueur]
        self.playerMove = None
        self.aiMove = None

    def update_player_move(self, move):
        """
        Met à jour le mouvement du joueur.

        Args:
            move (int): Le mouvement du joueur. Doit être 1, 2 ou 3.
        """
        self.playerMove = move

    def generate_ai_move(self):
        """
        Génère un mouvement aléatoire pour l'IA et l'affecte à aiMove.
        """
        self.aiMove = random.randint(1, 3)

    def update_scores(self):
        """
        Compare les mouvements du joueur et de l'IA et met à jour les scores en conséquence.
        Réinitialise ensuite les mouvements pour le prochain tour.
        >>> model = GameModel()
        >>> model.playerMove = 1  # Joueur choisit Pierre (1)
        >>> model.aiMove = 2      # IA choisit Papier (2)
        >>> model.update_scores()
        >>> model.scores    # IA gagne, score de l'IA augmenté de 1
        [1, 0]

        >>> model.playerMove = 1  # Joueur choisit Pierre (1)
        >>> model.aiMove = 3      # IA choisit Ciseaux (3)
        >>> model.update_scores()
        >>> model.scores # Joueur gagne, score du Joueur augmenté de 1
        [1, 1]


        >>> model.playerMove = 2  # Joueur choisit Papier (2)
        >>> model.aiMove = 2      # IA choisit Papier (2)
        >>> model.update_scores()
        >>> model.scores # Égalité, aucun score n'augmente
        [1, 1]

        >>> model.playerMove = 1  # Joueur choisit Pierre (1)
        >>> model.aiMove = 3      # IA choisit Ciseaux (3)
        >>> model.update_scores()
        >>> model.scores # Joueur gagne, score du Joueur augmenté de 1
        [1, 2]

        >>> model.playerMove = None
        >>> model.aiMove = None
        >>> model.scores # Les mouvements sont réinitialisés, aucun score ne change
        [1, 2]
        """
        if self.playerMove is not None and self.aiMove is not None:
            if (self.playerMove == 1 and self.aiMove == 3) or \
               (self.playerMove == 2 and self.aiMove == 1) or \
               (self.playerMove == 3 and self.aiMove == 2):
                self.scores[1] += 1  # Joueur gagne

            elif (self.playerMove == 3 and self.aiMove == 1) or \
                 (self.playerMove == 1 and self.aiMove == 2) or \
                 (self.playerMove == 2 and self.aiMove == 3):
                self.scores[0] += 1  # IA gagne

            self.playerMove = None
            self.aiMove = None

    def get_scores(self):
        """
        Retourne les scores actuels de la partie.

        Returns:
            list: Une liste contenant les scores [score de l'IA, score du joueur].
        """
        return self.scores
