"""image 283x283 sans compression en 2'30  ;  image 283x283 avec c=10 en 3' """
import imageio as im
import numpy as np
import os as os
import math as math
os.chdir("C:\\Users\\valen\\Documents\\GitHub\\Compression_Image\\Python")#attention, definir le chemin d'accès de votre ordi!
from tipe import *
os.chdir("C:\\valentin\\MPSI\\TIPE\\images\\DCT")#attention, definir le chemin d'accès de votre ordi!
def CompDCT(Nom_entree,Nom_sortie,Decoupage,Quantification,Compression):
    N1=Nom_entree#sans extension
    N2=Nom_sortie+".png"
    d=Decoupage
    quant=Quantification
    c=Compression
    RGBdecom(N1,N1)
    taille=im.imread(N1+".png").shape;ligne=taille[0];colonne=taille[1]
    print(ligne,colonne)
    if ligne%d!=0:
        ligne=ligne//d+1
    else:
        ligne=ligne//d
    if colonne%d!=0:
        colonne=colonne//d+1
    else:
        colonne=colonne//d#necessaure car comme m est une liste de matrices, elle n a pas de longueur.
    nbrbloc=ligne*colonne
    t=MatDCT(d)
    ti=InvMat(t)
    print(t,ti)
    rgb=['R','G','B']# pour traiter les matrices des trois couleurs
    for k in range(0,3):#il faudra faire en sorte de traiter les trois couleurs
        print("couleur",rgb[k])
        nb=str(N1+str(rgb[k])+".png")
        m=SecNxN(nb,d)
        #print(m)
        #print(nbrbloc)
        for j in range(0,nbrbloc):
            m[j]=mcentvs(m[j])
            print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",m[j])
            #print(t,m[j],j)
            a=MultMat(t,m[j])
            b=MultMat(a,ti)#matrice dans la nouvelle base
            if c!=0:# la compression supprime tous les coefs à valuer absolue inférieure à c
                q=matQuant(quant)
                for l in range(8):
                    for i in range(8):
                        b[l][i]=b[l][i]/q[l][i]
                for l in range(8):
                    for i in range(8):
                        if abs(b[l][i])<=c:
                            b[l][i]=0
                for l in range(8):
                    for i in range(8):
                        b[l][i]=b[l][i]*q[l][i]
            a=MultMat(ti,b)
            b=MultMat(a,t)#retourn dans la base de depart
            print("test",m[j])#retourne la matrice dans la nouvelle base et compressée(pb,pas d'image sous forme compressee, pas moins lourde en tout cas)
        print("a recomposer",m)
        f=recomNxN(m)
        f=pcentvs(f)
        im.imsave(str(N1+"comp"+str(rgb[k])+".png"),f)
    Nf=N1+"comp"
    print(Nf)
    I=RGBrecom(Nf,N2)