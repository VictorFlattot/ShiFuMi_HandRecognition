import random
import cv2
from HandDetectorFiles import HandDetector
from Utility import overlayPNG
import time

# Initialiser la capture vidéo de la webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Initialiser le détecteur de mains
detector = HandDetector(maxHands=1)

# Initialiser le timer, l'état du résultat, et le démarrage du jeu
timer = 0
stateResult = False
startGame = False

# Initialiser les scores [IA, Joueur]
scores = [0, 0]

# Boucle principale
while True:
    # Lire l'image de la webcam
    imgBG = cv2.imread("withwebcam/Resources/Background.png")
    success, img = cap.read()
    img = cv2.flip(img,1)

    # Redimensionner l'image
    imgScaled = cv2.resize(img, (0, 0), None, 1, 0.63)
    imgScaled = imgScaled[0:640, 0:480]
    #  Pour gerer les deplacements val + alors vers le b (1er col); - vers le h (1er col); + vers la d (2eme col); - vers la g(2eme col)
    # Détecter les mains
    hands, img = detector.findHands(imgScaled)  # avec dessin

    # Si le jeu est démarré
    if startGame & (scores[0]<=5 or scores[1]<=5) :
        # Si le résultat n'est pas encore affiché
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (607, 460), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 6)

            # Si le timer dépasse 3 secondes, afficher le résultat
            if timer > 3:
                stateResult = True
                timer = 0

                # Si une main est détectée
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    # Déterminer le mouvement du joueur en fonction des doigts levés
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3

                    # Générer un nombre aléatoire pour le mouvement de l'IA
                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(f'withwebcam/Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = overlayPNG(imgBG, imgAI, (149, 310))

                    # Si le joueur gagne
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1

                    # Si l'IA gagne
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1
    else : 
        scores[0] = 0
        scores[1] = 0

    # Superposer l'image de la webcam sur l'image de fond
    region_height = imgScaled.shape[0]
    bottom_position = 340  # Déplacer vers le bas de 5 pixels
    right_position = 769   # Déplacer vers la droite de 10 pixels
    imgBG[bottom_position:bottom_position + region_height, right_position:right_position + imgScaled.shape[1]] = imgScaled

    # Si le résultat est affiché, superposer l'image de l'IA
    if stateResult:
        imgBG = overlayPNG(imgBG, imgAI, (149, 340))

    # Afficher les scores
    cv2.putText(imgBG, str(scores[0]), (410, 250), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 127), 6)
    cv2.putText(imgBG, str(scores[1]), (1151, 250), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 127), 6)

    # Afficher les images
    cv2.imshow("BG", imgBG)

    # Attendre la touche 's' pour démarrer le jeu
    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
