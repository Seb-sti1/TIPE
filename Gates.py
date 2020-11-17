import numpy as np
import random as rand

H = (2**(-1/2))*np.array([[1, 1], [1, -1]])  # hadamard gate

X = np.array([[0, 1], [1, 0]])  # not gate


def mesure(Q):
    """
    Mesure le qubit Q
    :param: Q le gubit (numpy array)
    :return: int la resultat de la mesure (0 ou 1)
    """
    n = Q.shape[0]  # un qbit est une matrice colonne

    R = range(n)
    Prob = [Q[k, 0]**2 for k in range(n)]

    return rand.choices(R, Prob)[0]  # un seul choix demandé

