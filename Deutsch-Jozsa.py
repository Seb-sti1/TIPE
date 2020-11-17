import math as ma
import random as rand
import time as time
import numpy as np
import Gates as G
import Fonctions as Fonc

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
        print("La fonction choisie est constante")
        value = rand.choice([True, False])

        resultat = [value for k in range(2 ** n)]
    else:
        print("La fonction choisie est Balancée")
        resultat = [False for k in range(2 ** n)]  # on remplit le tableau de False
        possibilite = [k for k in range(2 ** n)]  # tous les numero possible

        for k in range(2 ** (n - 1)):  # choix des cases True
            choix = rand.choice(possibilite)

            supprime_element_list(possibilite, choix)  # on enleve le numero choisi
            resultat[choix] = True

    return resultat


def fonction_vers_oracle(f):
    """

    :param f:
    :return:
    """
    n = int(ma.log(len(f), 2))

    O = np.zeros((2 ** (n + 1), 2 ** (n + 1)))

    for i in range(2 ** (n + 1)):
        b = Fonc.base2(i)  # numero de la ligne en base 2 (correspond au qbit entrant dans l'oracle)
        b = b + [0] * (2 ** n - len(b))  # on complète le début pour avoir les zeros "inutiles"

        k = Fonc.base10(b[1:])  # n premier chiffre du qbit en base 10

        v = (f[k] + b[0]) % 2  # calcul de la valeur n+1 ieme suite au passage
        r = Fonc.base10([v] + b[1:])  # calcul du qbit complet resultant de l'opération

        O[i, r] = 1  # change la ligne i, colonne r en 1

    return O


def determination_classique(f):
    """
    Algorithme qui détermine si la fonction est constante ou balancée (de manière déterministe)
    :param f: la fonction
    :return: booléen : True => constante, False => balancée
    """
    n = int(ma.log(len(f), 2))

    first = f[0]

    for k in range(2 ** (n - 1) + 1):
        if first != f[k]:  # si on trouve une valeur differente de la première
            return False  # la fonction est balancée

    return True  # Si on a trouvé 2**(n-1) + 1 valeurs identique, la fonction est constante


# ============= Exemple ===========

for k in range(3):
    print("Essaie " + str(k))

    n = 5
    f = fonction_constante_ou_balancee(n)
    oracle = fonction_vers_oracle(f)

    # === Classique ===

    if determination_classique(f):
        print("Classique trouve : Constante")
    else:
        print("Classique trouve : Balancé")

    # === Quantique ===

    qbit_zero = np.array([[1], [0]])  # Qbit |0>
    qbit_un = np.array([[0], [1]])  # Qbit |1>

    # Etat de départ :

    Q0 = qbit_zero
    for k in range(n - 1):
        Q0 = Fonc.produitKronecker(Q0, qbit_zero)
    Q0 = Fonc.produitKronecker(Q0, qbit_un)

    # Portes hadamard

    H = G.H
    for k in range(n):
        H = Fonc.produitKronecker(H, G.H)

    Q1 = np.dot(H, Q0)

    # Oracle

    Q2 = np.dot(oracle, Q1)

    # Portes hadamard fin

    Q3 = np.dot(H, Q2)

    # print(Q0)
    # print(Q1)
    # print(Q2)
    # print(Q3)
    r = G.mesure(Q3)  # LA mesure

    if r == 0 or r == 1:
        print("Quantique trouve : Constante")
    else:
        print("Quantique trouve : Balancé")
