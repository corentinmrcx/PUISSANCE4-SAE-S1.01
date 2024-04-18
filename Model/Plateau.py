from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list:
    """
    Fonction qui crée un tableau 2D vide avec const.NB_LINES et const.NB_COLUMNS

    :return: retroune un tableau 2D
    """
    plateau = []
    for i in range(const.NB_LINES):
        plateau2 = []
        for j in range(const.NB_COLUMNS):
            plateau2.append(None)
        plateau.append(plateau2)
    return plateau

def placerPionPlateau(plateau: list, pion: dict, num_col: int)->int:
    """
    Fonction qui place un pion dans la colonne
    Le pion tombe jusqu'à ce qu'il rencontre un autre pion ou si il rencontre la dernière ligne,
    la fonction renvoie la ligne à laquelle le pion est placer

    :param plateau: tableau 2D contenant const.NB_LINES et const.NB_COLUMNS
    :param pion: dictionnaire représentant un pion
    :param num_col: entier compris entre 0 et const.NB_COLUMNS-1
    :return: retourne le numéro de la ligne
    """
    if not type_plateau(plateau):
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if not type_pion(pion):
        raise TypeError("placerPionPlateau : Le second paramètre n'est pas un pion")
    if type(num_col) != int:
        raise TypeError("placePionPlateau : Le troisième paramètre n'est pas un entier")
    if num_col < 0 or num_col >= const.NB_COLUMNS:
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {num_col} n'est pas correcte")

    num_ligne = -1
    if plateau[0][num_col] != None:
        return num_ligne
    else:
        num_ligne = 0
    pionPlacer = False
    while num_ligne <= 5 and not pionPlacer:
        if plateau[num_ligne][num_col] != None:
            plateau[num_ligne-1][num_col] = pion
            ligne = num_ligne - 1
            pionPlacer = True
        else:
            num_ligne += 1
    if pionPlacer == False and plateau[5][num_col] == None:
        plateau[5][num_col] = pion
        ligne = 5
        pionPlacer = True
    return ligne

def detecter4horizontalPlateau(plateau: list, couleur: int)-> list:
    """
    Fonction qui retourne une liste vide s'il n'y a aucune série de 4 pions alignés sinon une liste de pions de la
    couleur données

    :param plateau: liste 2D représentant le plateau
    :param couleur: entier qui vaut 1 ou 0
    :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
    """

    if not type_plateau(plateau):
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4horizontalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    liste_serie = []
    for lignes in plateau:
        for i in range(len(lignes)-3):
            if lignes[i] != None and lignes[i+1] != None and lignes[i+2] != None and lignes[i+3] != None:
                serie_pion = [lignes[i],lignes[i+1],lignes[i+2],lignes[i+3]]
                if getCouleurPion(serie_pion[0]) == couleur and  getCouleurPion(serie_pion[1]) == couleur and  getCouleurPion(serie_pion[2]) == couleur and  getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def detecter4verticalPlateau(plateau: list, couleur: int)-> list:
    """
    Fonction qui retourne une liste vide s'il n'y a aucune série de 4pions de la couleur données alignés verticalement,
    sinon une liste de ces pions qui sont alignés par 4 et vérifiant les conditions suivantes.

    :param plateau: liste 2D représentant le plateau
    :param couleur: entier qui vaut 1 ou 0
    :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    liste_serie = []
    for colonne in range(len(plateau[0])):
        for ligne in range(len(plateau) - 3):
            if (plateau[ligne][colonne] != None and plateau[ligne + 1][colonne] != None and plateau[ligne + 2][colonne] != None and plateau[ligne + 3][colonne] != None):
                serie_pion = [plateau[ligne][colonne], plateau[ligne + 1][colonne], plateau[ligne + 2][colonne],
                              plateau[ligne + 3][colonne]]
                if (getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur):
                    liste_serie.extend(serie_pion)
    return liste_serie

p = [[{'Couleur': 1, 'Identifiant': None}, None, None, {'Couleur': 1, 'Identifiant': None}, None, None, None], [{'Couleur': 1, 'Identifiant': None}, None, None, {'Couleur': 1, 'Identifiant': None}, None, None, None], [{'Couleur': 1, 'Identifiant': None}, None, None, {'Couleur': 1, 'Identifiant': None}, None, None, None], [{'Couleur': 1, 'Identifiant': None}, {'Couleur': 1, 'Identifiant': None}, None, {'Couleur': 1, 'Identifiant': None}, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None]]
print(detecter4verticalPlateau(p, 1))

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int)->list:
    """
    - Fonction qui  retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée alignés
    sur une diagonale « directe », sinon une liste de ces pions qui sont alignés par 4.

        - Si 5 pions sont alignés : la fonction renverra les 4 premiers pions seulement (avec les plus petits indices)
        - La liste retourner peut contenir plusieurs séries de 4 pions, et pas juste une seule.

        :param plateau: liste 2D représentant le plateau
        :param couleur: entier qui vaut 1 ou 0
        :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
        """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")

    liste_serie = []
    for lignes in range(len(plateau)-3):
        for colonnes in range(len(plateau[lignes])-3):
            if plateau[lignes][colonnes] != None and plateau[lignes+1][colonnes+1] != None and plateau[lignes+2][colonnes+2] != None and plateau[lignes+3][colonnes+3] != None:
                serie_pion = [plateau[lignes][colonnes],plateau[lignes+1][colonnes+1],plateau[lignes+2][colonnes+2],plateau[lignes+3][colonnes+3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int)-> list:
    """
    Fonction qui  retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée
    alignés sur une diagonale « indirecte », sinon une liste de ces pions qui sont alignés par 4.

        - Si 5 pions sont alignés : la fonction renverra les 4 premiers pions seulement (avec les plus petits indices)
        - La liste retourner peut contenir plusieurs séries de 4 pions, et pas juste une seule.

    :param plateau: liste 2D représentant le plateau
    :param couleur: entier qui vaut 1 ou 0
    :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4diagonaleIndirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")

    liste_serie = []
    for lignes in range(3,len(plateau)):
        for colonnes in range(lignes-3):
            if plateau[lignes][colonnes]!=None and plateau[lignes-1][colonnes+1] != None and plateau[lignes-2][colonnes+2] != None and plateau[lignes-3][colonnes+3] != None:
                serie_pion = [plateau[lignes][colonnes],plateau[lignes-1][colonnes+1],plateau[lignes-2][colonnes+2],plateau[lignes-3][colonnes+3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def getPionsGagnantsPlateau(plateau: list)->list:
    """
    Fonction qui fait une liste de toutes les séries de 4 pions alignés en prenant en compte les deux couleur

    :param plateau: liste 2D représentant un plateau
    :return: retourne une liste des pions gagnants
    """
    if not type_plateau(plateau):
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n'est pas un plateau")
    liste_pions_gagnants = []

    # on récupère les pions gagnants jaunes
    liste_pions_gagnants.extend(detecter4verticalPlateau(plateau, 0))
    liste_pions_gagnants.extend(detecter4horizontalPlateau(plateau, 0))
    liste_pions_gagnants.extend(detecter4diagonaleDirectePlateau(plateau, 0))
    liste_pions_gagnants.extend(detecter4diagonaleIndirectePlateau(plateau,0))

    # on récupère les pions gagnants rouges
    liste_pions_gagnants.extend(detecter4verticalPlateau(plateau, 1))
    liste_pions_gagnants.extend(detecter4horizontalPlateau(plateau, 1))
    liste_pions_gagnants.extend(detecter4diagonaleDirectePlateau(plateau, 1))
    liste_pions_gagnants.extend(detecter4diagonaleIndirectePlateau(plateau, 1))
    return liste_pions_gagnants

def isRempliPlateau(plateau: list)-> bool:
    """
    Fonction qui renvoie True si le plateau est rempli, False si ce n'est pas le cas

    :param plateau: liste 2D représentant un plateau
    :return: un booléen
    """
    if not type_plateau(plateau):
        raise TypeError("isRempliPlateau : Le paramètre n'est pas un plateau")
    pions_premiere_ligne = []
    for col in range(len(plateau[0])):
        if plateau[0][col] != None:
            pions_premiere_ligne.append(plateau[0][col])
        else:
            pions_premiere_ligne = []
    return len(pions_premiere_ligne) == const.NB_COLUMNS

def placerPionLignePlateau(plateau: list, pion: dict,num_ligne: int, left: bool):
    """
    Fonction qui permet de placer des pions par la gauche ou par la droite du plateau en fonction
    du numéro de la ligne passé en paramètre ainsi que du coté représenté par le booléen "left"

    - Ajout de pion par la gauche : (left = True)
    - Ajout de pion par la droite : (left = False)

    :param plateau: liste 2D représentant un plateau
    :param pion: dictionnaire représentant un pion
    :param num_ligne: entier qui correspond à un numéro de ligne
    :param left: indique par où on insère le pion
    :return: retourne un tuple contenant la liste des pions poussés et un entier qui correspond
            à la ligne du dernier pion de la liste (None si pion change pas de ligne)
    """

    if not type_plateau(plateau):
        raise TypeError("placerPionLignePlateau : Le premier paramètre n'est pas un plateau")
    if not type_pion(pion):
        raise TypeError("placerPionLignePlateau : Le second paramètre n'est pas un pion")
    if type(num_ligne) != int:
        raise TypeError("placerPionLignePlateau : Le troisième paramètre n'est pas un entier")
    if num_ligne < 0 or num_ligne > const.NB_LINES-1:
        raise ValueError(f"placerPionLignePlateau : Le troisième paramètre {num_ligne} ne désigne pas une ligne")
    if type(left) is not bool:
        raise TypeError("placerPionLignePlateau : Le quatrième paramètre n'est pas un booléen")

    pions_pousses = [pion]
    tomber = None

    #Placement du pion par la gauche (left=True)
    if left:
        i = 0
        while i < const.NB_COLUMNS and plateau[num_ligne][i] is not None:
            pions_pousses.append(plateau[num_ligne][i])
            i += 1

        for k in range(len(pions_pousses) - 1):
            plateau[num_ligne][k] = pions_pousses[k]

        del pions_pousses[1]

        tomber = num_ligne
        while tomber + 1 < const.NB_LINES and plateau[tomber + 1][len(pions_pousses) - 1] is None:
            plateau[tomber + 1][len(pions_pousses) - 1] = plateau[tomber][len(pions_pousses) - 1]
            plateau[tomber][len(pions_pousses) - 1] = None

    #Placement du pion par la droite (left=False)
    else:
        i = const.NB_COLUMNS - 1
        while i >= 0 and plateau[num_ligne][i] is not None:
            pions_pousses.append(plateau[num_ligne][i])
            i -= 1

        for k in range(min(len(pions_pousses), const.NB_COLUMNS)):
            plateau[num_ligne][const.NB_COLUMNS - 1 - k] = pions_pousses[k]

        del pions_pousses[const.NB_COLUMNS-1]

        tomber = num_ligne
        while tomber + 1 < const.NB_LINES and plateau[tomber + 1][const.NB_COLUMNS - 1 - len(pions_pousses) + 1] is None:
            plateau[tomber + 1][const.NB_COLUMNS - 1 - len(pions_pousses) + 1] = plateau[tomber][const.NB_COLUMNS - 1 - len(pions_pousses) + 1]
            plateau[tomber][const.NB_COLUMNS - 1 - len(pions_pousses) + 1] = None
            tomber += 1

    return pions_pousses, tomber

def encoderPlateau(plateau: list) -> int:
    """
    Fonction qui permet d'encoder le plateau en une chaine de caractère

    :param plateau: Plateau séléctionné
    :return: Une chaîne de caractères représentant l'encodage du plateau.
    """
    if type_plateau(plateau) == False:
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau")

    encodage = ""
    for i in range(const.NB_LINES):
        for j in range(const.NB_COLUMNS):
            if plateau[i][j] == None:
                encodage += "_"
            elif plateau[i][j][const.COULEUR] == 0:
                encodage += "J"
            else:
                encodage += "R"
    return encodage
def isPatPlateau(plateau: list, histoPlat: dict) -> bool:
    """
    Fonction qui permet de vérifier si le plateau apparait 5 fois dans l'historigramme des plateaux.

    :param plateau: Plateau séléctionné
    :param histoPlat: Dictionnaire représentant l'histogramme des plateaux
    :return: Retourne True si le plateau apparait pour la cinquième fois, False sinon
    """
    if type_plateau(plateau) == False:
        raise TypeError("isPatPlateau : Le premier paramètre n'est pas un plateau")
    if type(histoPlat) != dict:
        raise TypeError("isPatPlateau : Le deuxième paramètre n'est pas un dictionnaire")

    clePlateau = encoderPlateau(plateau)
    res = False
    if clePlateau in histoPlat:
        histoPlat[clePlateau] += 1
        if histoPlat[clePlateau] >= 5:
            res = True
    else:
        histoPlat[clePlateau] = 1

    return res