from GameController import GameController


def main():
    """
    Fonction principale pour initialiser et démarrer le contrôleur de jeu.
    Crée une instance de GameController et appelle la méthode run pour démarrer le jeu.
    """
    game_controller = GameController()
    game_controller.run()


if __name__ == "__main__":
    """
    Point d'entrée principal du script. 
    Si ce script est exécuté comme programme principal (et non importé comme module), 
    il appelle la fonction main pour démarrer le jeu.
    """
    main()
