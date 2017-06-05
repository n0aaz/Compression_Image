import imageio as im
import numpy as np
import os as os
import math as math
from tipe_bis import *

os.chdir("/home/n0aaz/compression/Compression_Image/Python")#attention, definir le chemin d'accès de votre ordi!
os.chdir("/home/n0aaz/compression/Compression_Image/Python")#attention, definir le chemin d'accès de votre ordi!


def compDCT2(nom,decoupage,quantification,seuil):
    n=nom;d=decoupage;q=quantification;z=seuil;lf=[]
    #imp=input("impression des photos intermédiares:\n1=oui\n0=non\n")
    dctmat=matDCT(d)#matrice du changement de base
    
    #enreg=open('compress.txt','w')
    precision=0 #nombre de chiffres significatifs
    
    invdct=np.linalg.inv(dctmat)#matrice de changement de base inverse
    
    matquant=quantMat(q)#donne une matrice de quantification au niveau choisi
    i=lectImage(n)#i donne la matrice de l'image n
    a=decomCouleur(i);dim=a[0][2];ligne=a[0][0];colonne=a[0][1]#dimension de la matrice (1=noir et blanc;3=couleur)
    
    
    for k in range(1,dim+1):#parcours toutes les couleurs
        mat=a[k]#matrice de la couleur traitée
        mat=retail(mat,d)#donne une matrice de taille multiple du découpageS
        lmat=decoupNxN(mat,d)#decoupe la matrice pour donner une liste de matrices
        
        enreg=open(str(k)+'.txt','w')
        
        for j in range(len(lmat)): #génération et compression de la matrice
            matsec=moins127(np.int_(lmat[j]))
            matsec=dctmat.dot(matsec.dot(invdct))#on obtient matsec dans la base DCT
            
            
            '''if z!=0: #compression avec perte
                for l in range(d):
                    for o in range(d):
                        if abs(matsec)[l][o]<=z:#compression
                            matsec[l][o]=0
            '''
            matsec=np.round(matsec/matquant)
            for k in rle(diago(matsec)):
                enreg.write(str(k[0])+','+str(int(k[1]))+'\n')
            enreg.write('\n')

            #print(rle(diago(matsec)))
            #print(lecture('compress.txt'))
            #print(dediago(unrle(rle(diago(matsec)),d**2))-matsec) #petite vérfication pour voir si la compression/décompression fonctionne
                                                                  #Si c'est le cas ça devrait nous renvoyer uniquement des matrices nulles
            matsec=matsec*matquant

            matsec=invdct.dot(matsec.dot(dctmat))
            #print(matsec)
            
            lmat[j]=matsec
        mat=recoNxN(lmat,ligne,colonne,d)
        mat=redim(mat,ligne,colonne)
        lf.append(mat)
    matc=recoRGB(lf)
    saveIm(matc,n)
    #print(len(lecture('compress.txt')[0]))

compDCT2('paysage.bmp',8,1,50)
