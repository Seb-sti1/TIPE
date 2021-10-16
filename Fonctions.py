# @author Seb-sti1

import numpy as np
import matplotlib.pyplot as plt
import math as ma


def base2(n):
    """
    Renvoie une liste de l'écriture en base 2 de n. Le poids correspond à l'indice.
    :param n: Le nombre
    :return: La liste de l'écriture binaire
    """
    L = []

    if n == 0:
        L = [0]
    else:
        L = []
        i = n
        while i > 0:
            if i % 2 == 0:
                L.append(0)
            else:
                L.append(1)

            i = i // 2

    return L


def base10(L):
    """
    Renvoie le nombre à partie de son écriture en base 2. C'est la fonction reciproque de base2
    :param L: La liste
    :return: le nombre decimal
    """
    n = len(L)

    S = 0

    for k in range(n):
        S += L[k] * 2 ** k

    return S


def produit_matriciel(A, B):
    """
    A, B des matrices de taille nA, pA et nB, pB tel que pA = nB. Renvoie leur produit matriciek

    :param A: une matrice
    :param B: une matrice
    :return: A x B
    """

    nA, pA = np.shape(A)
    nB, pB = np.shape(B)

    if nB != pA:
        raise Exception("Produit matriciel impossible")

    R = np.zeros((nA, pB))

    for i in range(nA):
        for j in range(pB):
            for k in range(pA):
                R[i, j] += A[i, k] * B[k, j]

    return R


def produit_kronecker(A, B):
    """
    A, B des matrices de taille quelconque. Renvoie leur produit de Kronecker

    :param A: une matrice
    :param B: une matrice
    :return: A x B (avec x le produit de Kronecker)
    """
    nA, pA = A.shape
    nB, pB = B.shape

    n, p = nA * nB, pA * pB

    R = np.zeros((n, p))

    for iA in range(nA):
        for jA in range(pA):
            for iB in range(nB):
                for jB in range(pB):
                    R[iA * nB + iB, jA * pB + jB] = A[iA, jA] * B[iB, jB]

    return R


def plot_qubit(Q, coef=False):
    n = np.shape(Q)[0]

    name = []

    for k in range(n):
        s = "$|"

        binaire = base2(k)
        binaire = (int(ma.log(n, 2)) - len(binaire)) * [0] + [binaire[len(binaire) - k - 1] for k in range(len(binaire))]

        for e in binaire:
            s += str(e)

        s += "\\rangle$"
        name.append(s)

    x = [1.5*k for k in range(n)]

    if not coef:
        values = [abs(Q[k, 0]) ** 2 for k in range(n)]
    else:  # pas de partie imaginaire
        values = [Q[k, 0] for k in range(n)]

    plt.xticks(x, labels=name, rotation=90)
    plt.bar(x, values)

    plt.show()
