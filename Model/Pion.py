# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Fonction qui détermine si le paramètre peut-être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(couleur: int) -> dict:
    """
    Fonction qui permet de construire un pion selon la couleur reçu en paramètre

    :param couleur: Entier qui désigne la couleur du pion
    :return: Retourne un pion construit avec la couleur
    """
    if couleur == 1:
        pion = {const.COULEUR: const.COULEURS[1], const.ID: None}
    elif couleur == 0:
        pion = {const.COULEUR: const.COULEURS[0], const.ID: None}
    if type(couleur) != int:
        raise TypeError("construirePion: Le paramètre n'est pas de type entier")
    if couleur != 1 and couleur != 0:
        raise ValueError("construirePion : la couleur (valeur_du_paramètre) n'est pas correct")
    return pion
def getCouleurPion(pion: dict) -> int:
    """
    Fonction qui renvoie la couleur du pion passé en paramètre

    :param pion: Dictionnaire qui représente l'object pion
    :return: Retourne la couleur du pion
    """
    if not type_pion(pion):
        raise TypeError("getCouleurPion : le paramètre n'est pas un pion")
    return pion[const.COULEUR]

def setCouleurPion(pion: dict, couleur: int) -> None:
    """
    Fonction qui modifie la couleur du pion passé en paramètre avec la nouvelle couleur

    :param pion: Dictionnaire qui représente l'object pion
    :param couleur: Entier qui désigne la couleur du pion
    :return: None
    """
    if not type_pion(pion):
        raise TypeError("setCouleurPion : Le premier paramètre n'est pas un pion")
    if type(couleur) != int:
        raise TypeError("setCouleurPion : Le second paramètre n'est pas une couleur")

    if couleur != 0 and couleur != 1:
        raise ValueError("setCouleurPion : Le second paramètre n'est pas un pion")

    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion: dict) -> int:
    """
    Fonction qui renvoie l'identifiant du pion passé en paramètre

    :param pion: Dictionnaire qui représente l'object pion
    :return: Entier qui correspond a l'identifiant
    """
    if not type_pion(pion):
        raise TypeError("getIdPion : Le paramètre n'est pas un pion")
    return pion[const.ID]

def setIdPion(pion: dict, valeurID: int) -> None:
    """
    Fonction qui modifie l'identifiant du pion passé en paramètre

    :param pion: Dictionnaire qui représente l'object pion
    :param valeurID: Valeur de l'entier que l'on veut comme identifiant
    :return: Retourne Rien
    """
    if not type_pion(pion):
        raise TypeError("setIdPion : Le premier paramètre n'est pas un pion")
    if type(valeurID) != int:
        raise TypeError("setIdPion : Le second paramètre n'est pas un entier")

    pion[const.ID] = valeurID
    return None
