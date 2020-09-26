import math as ma
import random as rand
import time as time
import numpy as np
import Gates

"""
La fonction f dont on veut savoir si elle est constante ou balancée est représentée par un tableau de booléen
"""


def supprime_element_list(list, element):
    """
    Supprime un element d'une liste
    :param list: la liste
    :param element: l'element à supprimer
    :return: None
    """

    for k in range(len(list)):
        if list[k] == element:
            list.pop(k)
            break


def fonction_constante_ou_balancee(n):
    """
    Creer une liste (représentant la fonction) de 2^n. La liste contient soit que des True ou des Faux (fonction constante)
    soit 2^{n-1} True et 2^{n-1} False
    :param n:
    :return: une liste de booléen de taille 2^n
    """
    # on modifie la seed de la librairie pour avoir des nombres le plus aleatoire posible
    rand.seed(time.time())

    # la liste resultat
    resultat = []

    est_constante = rand.choice([True, False])  # choix entre constante ou balancé

    if est_constante:
        print("Constante")
        value = rand.choice([True, False])

        resultat = [value for k in range(2**n)]
    else:
        print("Balancée")
        resultat = [False for k in range(2**n)]  # on remplit le tableau de False
        possibilite = [k for k in range(2**n)]  # tous les numero possible

        for k in range(2**(n-1)):  # choix des cases True
            choix = rand.choice(possibilite)

            supprime_element_list(possibilite, choix)  # on enleve le numero choisi
            resultat[choix] = True

    return resultat


def fonction_vers_porte(f):
    """

    :param f:
    :return:
    """
    n = int(ma.log(len(f), 2))

    np.zeros((2, n))



    return


def determination_classique(oracle):
    """
    Algorithme qui détermine si la fonction est constante ou balancée (de manière déterministe)
    :param oracle: un oracle de la fonction
    :return: booléen : True => constante, False => balancée
    """
    n = int(ma.log(len(oracle), 2))

    first = oracle[0]

    for k in range(2**(n-1) + 1):
        if first != oracle[k]:  # si on trouve une valeur differente de la première
            return False  # la fonction est balancée

    return True  # Si on a trouvé 2**(n-1) + 1 valeurs identique, la fonction est constante

