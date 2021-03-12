import numpy as np
import math as ma
import random as rd
import matplotlib.pyplot as plt

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

H=np.array([[1,1],[1,-1]])/ma.sqrt(2)
EF0=np.array([[1],[0]])

def ProdM(A,B):
    """ produit matriciel AxB"""
    a=np.shape(A)
    b=np.shape(B)
    C=np.zeros((a[0],b[1]))
    for i in range(a[0]):
        for j in range(b[1]):
            for k in range(a[1]):
                C[i,j]+=A[i,k]*B[k,j]
    return C

def Transpo(A):
    a=np.shape(A)
    C=np.zeros((a[1],a[0]))
    for i in range(a[0]):
        for j in range(a[1]):
            C[j,i]=A[i,j]
    return C

def Kronecker(A,B):
    a=np.shape(A)
    b=np.shape(B)
    C=np.zeros((a[0]*b[0],a[1]*b[1]))
    for i in range(a[0]):
        for j in range(a[1]):
            for k in range(b[0]):
                for l in range(b[1]):
                    C[i*b[0]+k,j*b[1]+l]=A[i,j]*B[k,l]
    return C

def KroneckerIt(A,n):
    """n>1"""
    M=np.copy(A)
    for k in range(n-1):
        M=Kronecker(M,A)
    return M

def Grover(N):
    """N est le nombre de qubits et recherche une unique solution"""
    #Initialisation des portes et de la solution
    S=rd.randint(0,2**N-1)
    Uf=-np.eye(2**N)     #matrice de l'oracle
    Uf[S,S]=1
    Hn=KroneckerIt(H,N)
    E=KroneckerIt(EF0,N)    #qubits équilibrés à l'entrée de l'algorithme
    tE=KroneckerIt(Transpo(EF0),N)
    Z=2 * ProdM(E,tE) - np.eye(2**N)
    G=ProdM(ProdM(ProdM(Hn,Z),Hn),Uf)

    #Algorithme
    Psi=np.copy(E)
    Psi=ProdM(Hn,Psi)
    M=ma.floor(ma.pi/4*ma.sqrt(2**N))
    for k in range(M):
        Psi=ProdM(G,Psi)

    #Affichage
    PsiList=[Psi[k,0] for k in range(2**N)]
    PsiListAmp=[Psi[k,0]**2 for k in range(2**N)]
    plt.subplot(1,2,1)
    plt.bar(range(2**N),PsiList,0.5,align='center',color='blue',edgecolor='mediumblue')
    plt.title("Coefficients", fontsize=20)
    plt.xlim(-1,2**N)
    plt.subplot(1,2,2)
    plt.bar(range(2**N),PsiListAmp,0.5,align='center',color='blue',edgecolor='mediumblue')
    plt.xlim(-1,2**N)
    plt.title("Amplitude de probabilité", fontsize=20)

    plt.show()

    #return Psi,S

def GroverBis(N,NbSol):
    #Initialisation des portes et de la solution
    S=rd.sample(range(2**N-1),NbSol)
    Uf=-np.eye(2**N)     #matrice de l'oracle
    for i in S:
        Uf[i,i]=1

    Hn=KroneckerIt(H,N)
    E=KroneckerIt(EF0,N)    #qubits équilibrés à l'entrée de l'algorithme
    tE=KroneckerIt(Transpo(EF0),N)
    Z=2 * ProdM(E,tE) - np.eye(2**N)
    G=ProdM(ProdM(ProdM(Hn,Z),Hn),Uf)

    #Algorithme
    Psi=np.copy(E)
    Psi=ProdM(Hn,Psi)
    theta = ma.asin(ma.sqrt(NbSol/2**N))
    M=ma.floor(ma.pi/4/theta-1/2)
    for k in range(M):
        Psi=ProdM(G,Psi)

    #Affichage
    Psilist=[Psi[k,0] for k in range(2**N)]
    plt.bar(range(2**N),Psilist,0.5,align='center',color='blue',edgecolor='mediumblue')
    plt.show()
    print(S)
