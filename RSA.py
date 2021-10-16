# @author Seb-sti1

import math as ma
import random as rand
import time as time


#
# Fonctions de vérification
#

def est_premier(n):
    """
    Si n est premier
    :param n:
    :return: boolean
    """

    for i in range(2, int(ma.sqrt(n)) + 1):
        # si i|n alors n pas premier
        if n % i == 0:
            return False

    return True


def euclide(a, b):
    """
    Realise l'algorithme d'Euclide sur a et b

    :param a:
    :param b:
    :return: PGCD(a, b)
    """
    u, v = abs(a), abs(b)

    while v != 0:
        u, v = v, u % v

    return u


def euclide_etendu(a, b):
    """
    Realise l'algorithme etendu d'Euclide sur a et b

    :param a:
    :param b:
    :return: (u, v) tq au + bv = 1; les coefficients de bézoux
    """
    r, u, v, r_, u_, v_ = abs(a), 1, 0, abs(b), 0, 1

    while r_ != 0:
        q = r//r_
        r, u, v, r_, u_, v_ = r_, u_, v_, r - q * r_, u - q * u_, v - q * v_

    return u, v


#
# Fonction de génération
#


def nbr_premier_aleatoire(max):
    """
    Generère aleatoirement des nombres premiers aleatoires strictement plus petit que n

    :param max:
    :return: p, q des entiers aleatoire premier
    """
    # on modifie la seed de la librairie pour avoir des nombres le plus aleatoire posible
    rand.seed(time.time())
    p, q = 0, 0

    # on choisit p
    while p == 0:
        # on prend un nombre aleatoire (de deux en deux pour eviter les nombres paires)
        candidat = rand.randrange(1, max, 2)

        # si il est premier on en a alors trouvé 1
        if est_premier(candidat):
            p = candidat

    # on choisit p
    while q == 0:
        # on prend un nombre aleatoire (de deux en deux pour eviter les nombres paires)
        candidat = rand.randrange(1, max, 2)

        # si on c'est pas déjà p
        if p != candidat:
            # si il est premier on en a alors trouvé 2
            if est_premier(candidat):
                q = candidat

    return p, q


def exposant(lambda_n, max):
    """
    l'exposant premier avec lambda_n et strictement inférieur à max

    Source : https://tools.ietf.org/html/rfc3447#section-3.1

    :param lambda_n:
    :param max:
    :return e:
    """
    e = 0

    while e == 0:
        # on choisit un nombre aleatoire
        candidat = rand.randrange(2, max)

        # si ils sont premier entre eux
        if euclide(candidat, lambda_n) == 1:
            e = candidat

    return e


def inverse_mod(e, mod):
    """
    Calcul l'inverse de e modulo mod

    :param e:
    :param mod:
    :return: d
    """
    # on calcul les coefficients dé bézout
    u, v = euclide_etendu(e, mod)
    # on a alors e*u + v*mod = 1 ie e*u % mod = 1

    # on applique l'opération modulo de python pour avoir un nombre positif
    return u % mod


#
# Chiffrement/ Dechiffrement
#


def RSA_entier(cle, M):
    """
    Chiffre/déchiffre M

    Sources :
    https://tools.ietf.org/html/rfc3447#section-5.1.1
    https://tools.ietf.org/html/rfc3447#section-5.1.2

    :param cle: (n, e) module de chiffrement et exposant
    :param M: entier à chiffrer
    :return:
    """
    n, e = cle

    if M < 0 or M >= n:
        raise Exception("M dois être compris entre 0 et n-1")

    return M**e % n


def RSA_texte(cle, texte):
    """
    Chiffre/Dechiffre texte

    :param cle:
    :param texte:
    :return:
    """
    c = ""

    # pour chaque lettre
    for lettre in texte:
        # on recupère le code ASCII
        ASCII = ord(lettre)

        # on chiffre
        C_ASCII = RSA_entier(cle, ASCII)

        # on prend la lettre correspondante
        c += chr(C_ASCII)

    return c

#
# Génération des cléfs
#


a = time.time()
max = 150

p, q = nbr_premier_aleatoire(max)  # nombre premier

n = p * q  # module de chiffrement
lambda_n = (p-1)*(q-1)

e = exposant(lambda_n, max)  # exposant de chiffrement
d = inverse_mod(e, lambda_n)  # exposant de dechiffrement

cle_public = (n, e)
cle_prive = (n, d)

print(cle_public)
print(cle_prive)

T = "Hello Github ! On fait nos TIPE !"
C = RSA_texte(cle_public, T)
print("Texte chiffré : ")  # + C)
print("Déchiffrement en cours...")
print("Texte déchiffré : " + RSA_texte(cle_prive, C))

b = time.time()
print(b-a)
