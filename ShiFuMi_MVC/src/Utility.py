def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    """
    Applique une image PNG avec transparence sur une autre image en utilisant le mélange alpha.
    La fonction gère les positions en dehors des limites, y compris les coordonnées négatives,
    en recadrant l'image à superposer en conséquence. Les bords sont lissés en utilisant le mélange alpha.

    Args:
        imgBack (numpy.ndarray): L'image d'arrière-plan, un tableau NumPy de forme (hauteur, largeur, 3) ou (hauteur, largeur, 4).
        imgFront (numpy.ndarray): L'image PNG d'avant-plan à superposer, un tableau NumPy de forme (hauteur, largeur, 4).
        pos (list): Une liste spécifiant les coordonnées x et y (en pixels) auxquelles superposer l'image.
                    Peut être négatif ou amener l'image à superposer à dépasser les limites.

    Returns:
        numpy.ndarray: Une nouvelle image avec la superposition appliquée, un tableau NumPy de forme comme `imgBack`.
    """
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape

    x1, y1 = max(pos[0], 0), max(pos[1], 0)
    x2, y2 = min(pos[0] + wf, wb), min(pos[1] + hf, hb)

    # Pour les positions négatives, changez la position de départ dans l'image à superposer
    x1_overlay = 0 if pos[0] >= 0 else -pos[0]
    y1_overlay = 0 if pos[1] >= 0 else -pos[1]

    # Calculez les dimensions de la tranche à superposer
    wf, hf = x2 - x1, y2 - y1

    # Si la superposition est complètement en dehors de l'arrière-plan, retournez l'arrière-plan original
    if wf <= 0 or hf <= 0:
        return imgBack

    # Extrayez le canal alpha de l'avant-plan et créez le masque inverse
    alpha = imgFront[y1_overlay:y1_overlay + hf, x1_overlay:x1_overlay + wf, 3] / 255.0
    inv_alpha = 1.0 - alpha

    # Extrayez les canaux RVB de l'avant-plan
    imgRGB = imgFront[y1_overlay:y1_overlay + hf, x1_overlay:x1_overlay + wf, 0:3]

    # Mélange alpha des avant-plans et arrière-plans
    for c in range(0, 3):
        imgBack[y1:y2, x1:x2, c] = imgBack[y1:y2, x1:x2, c] * inv_alpha + imgRGB[:, :, c] * alpha

    return imgBack
