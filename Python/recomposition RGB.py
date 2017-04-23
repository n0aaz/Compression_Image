import imageio as im
import numpy as np
def recomRGB(N1,N2):#ATTENTION: N1=image RGB, sans precision couleur ni extension,MAIS N2 a donner avec extension
    NR=N1+"R.png"#Noms complets de fichiers RGB
    NG=N1+"G.png"
    NB=N1+"B.png"
    R=im.imread(NR);G=im.imread(NG);B=im.imread(NB)#import des fichiers RGB
    M=[]#matrice de la l'image de sortie(ici sous forme de liste)
    T=R.shape;L=T[0];C=T[1]#défini la taille de limage des martices d'entrées
    R=np.reshape(R,(L*C,1));G=np.reshape(G,(L*C,1));B=np.reshape(B,(L*C,1))#fait des matrices lignes, permattant d'eviter une conversion en liste de tuples
    R=R.tolist();G.tolist();B=B.tolist()#conversion des matrices en liste(plus rapide pour python)
    for k in range(0,L*C):
        m=(R[k],G[k],B[k])
        M.append(m)
    M=np.reshape(M,(L,C,3))#le 3 permet de de redonner une troisieme dimension a la matrice, à cause des tuples de 3
    im.imsave(str(N2),M)#sauvegarde de l'image