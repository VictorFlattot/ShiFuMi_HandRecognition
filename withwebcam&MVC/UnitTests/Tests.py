import unittest
from GameModel import GameModel
from GameController import interpret_player_move


class TestAddition(unittest.TestCase):
    def test_update_scores(self):
        model = GameModel()
        model.playerMove = 1  # Joueur choisit Pierre (1)
        model.aiMove = 2  # IA choisit Papier (2)
        model.update_scores()

        self.assertEqual(model.scores, [1, 0])  # IA gagne, score de l'IA augmenté de 1

        model.playerMove = 1  # Joueur choisit Pierre (1)
        model.aiMove = 3  # IA choisit Ciseaux (3)
        model.update_scores()
        self.assertEqual(model.scores, [1, 1])  # Joueur gagne, score du Joueur augmenté de 1

        model.playerMove = 2  # Joueur choisit Papier (2)
        model.aiMove = 2  # IA choisit Papier (2)
        model.update_scores()
        self.assertEqual(model.scores, [1, 1])  # Égalité, aucun score n'augmente

        model.playerMove = 1  # Joueur choisit Pierre (1)
        model.aiMove = 3  # IA choisit Ciseaux (3)
        model.update_scores()
        self.assertEqual(model.scores, [1, 2])  # Joueur gagne, score du Joueur augmenté de 1

        model.playerMove = None
        model.aiMove = None
        self.assertEqual(model.scores, [1, 2])  # Les mouvements sont réinitialisés, aucun score ne change

    def test_interpret_player_move(self):
        res = interpret_player_move([0, 0, 0, 0, 0])
        self.assertEqual(res, 1)  # Tous les doigts abaissés, mouvement "Pierre"
        res = interpret_player_move([1, 1, 1, 1, 1])
        self.assertEqual(res, 2)  # Tous les doigts levés, mouvement "Papier"
        res = interpret_player_move([0, 1, 1, 0, 0])
        self.assertEqual(res, 3)  # Deux doigts levés, mouvement "Ciseaux" # Deux doigts levés, mouvement "Ciseaux"
        res = interpret_player_move([1, 0, 1, 1, 1])
        self.assertTrue(res is None)  # Mouvement non reconnu


if __name__ == '__main__':
    unittest.main()
