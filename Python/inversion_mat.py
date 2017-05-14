import numpy as np#  /!\ ATTENTION PAS DE SECURITE SI MATRICE NON INVERSIBLE !!!
np.set_printoptions(precision=5)#permet de ne pas avoir de chiffres en écriture décimale trop long
np.set_printoptions(suppress=True)#autorise la suppression automatique d'éléments du tableau(?)
def InvMat(M):
    T=M.shape;L=int(T[0])
    I=np.zeros([L,L])# création matrice identité
    for k in range(0,L):
        I[k][k]=1
    print(I)
    M=np.append(M,I,axis=1)#colle les matrices M et I
    print('1',M)
    for k in range(0,L-1):#création d'une matrice triangulaire supérieure
        for j in range(k+1,L):
            if M[k][k]!=0:
                A=M[j][k]/M[k][k]
                for l in range(0,2*L):
                    M[j][l]=M[j][l]-A*M[k][l]#/!\ PLUS D'ARRONDI ICI
    print('2',M)
    for k in range(1,L):#création de la matrice diagonale
        for j in range(0,k):
            if M[k][k]!=0:
                A=M[j][k]/M[k][k]
                for l in range(0,2*L):
                    M[j][l]=M[j][l]-A*M[k][l]#/!\ PLUS D'ARRONDI
    print('3',M)
    for k in range(0,L):
        A=M[k][k]
        for l in range(0,2*L):
            M[k][l]=M[k][l]/A
    print('4',M)
    for k in range(L-1,-1,-1):
        M=np.delete(M,(k),axis=1)#permet de supprimer la k-ème colonne de M
    return M