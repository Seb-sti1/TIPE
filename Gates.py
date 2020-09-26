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

    return rand.choices([0, 1], [Q[0]**2, Q[1]**2])

