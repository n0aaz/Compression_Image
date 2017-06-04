import imageio as im
import numpy as np
import os as os
import math as math
os.chdir("C:\\Users\\valen\\Documents\\GitHub\\Compression_Image\\Python")#attention, definir le chemin d'accès de votre ordi!
from tipe_bis import *
os.chdir("C:\\valentin\\MPSI\\TIPE\\images\\DCT")#attention, definir le chemin d'accès de votre ordi!
def compDCT2(nom,decoupage,quantification,seuil):
    n=nom;d=decoupage;q=quantification;z=seuil;lf=[]
    #imp=input("impression des photos intermédiares:\n1=oui\n0=non\n")
    dctmat=matDCT(d)#matrice du changement de base
    invdct=np.linalg.inv(dctmat)#matrice de changement de base inverse
    matquant=quantMat(q)#donne une matrice de quantification au niveau choisi
    i=lectImage(n)#i donne la matrice de l'image n
    a=decomCouleur(i);dim=a[0][2];ligne=a[0][0];colonne=a[0][1]#dimension de la matrice (1=noir et blanc;3=couleur)
    for k in range(1,dim+1):#parcours toutes les couleurs
        mat=a[k]#matrice de la couleur traitée
        mat=retail(mat,d)#donne une matrice de taille multiple du découpageS
        lmat=decoupNxN(mat,d)#decoupe la matrice pour donner une liste de matrices
        for j in range(len(lmat)):
            matsec=lmat[j]
            matsec=dctmat.dot(matsec.dot(invdct))#on obtient matsec dans la base DCT
            matsec=matsec/matquant
            if z!=0:
                for l in range(d):
                    for o in range(d):
                        if abs(matsec)[l][o]<=z:#compression
                            matsec[l][o]=0
            matsec=matsec*matquant
            matsec=invdct.dot(matsec.dot(dctmat))
            lmat[j]=matsec
        mat=recoNxN(lmat,ligne,colonne,d)
        mat=redim(mat,ligne,colonne)
        lf.append(mat)
    matc=recoRGB(lf)
    saveIm(matc,n)