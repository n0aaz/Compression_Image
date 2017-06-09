import imageio as im
import numpy as np
import os as os
import math as math

os.chdir("C:\\Users\\valen\\Documents\\GitHub\\Compression_Image\\Python")#attention, definir le chemin d'accès de votre ordi!
from tipe_bis import *
os.chdir("C:\\valentin\\MPSI\\TIPE\\images\\DCT")#attention, definir le chemin d'accès de votre ordi!


def compDCT2(nom,decoupage,quantification):
    n=nom;d=decoupage;q=quantification;lf=[]
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
        chemin=str(k)+'.txt'
        enreg=open(chemin,'w')
        
        for j in range(len(lmat)): #génération et compression de la matrice
            matsec=moins127(np.int_(lmat[j]))
            matsec=dctmat.dot(matsec.dot(invdct))#on obtient matsec dans la base DCT
            matsec=matsec/matquant
            
            dernier=rle(diago(matsec))[-1]
            for k in rle(diago(matsec)):
                if k != dernier:
                    enreg.write(str(k[0])+','+str(int(k[1]))+'/')
                else:
                    enreg.write(str(k[0])+','+str(int(k[1])))
            enreg.write('\n')

            #print(rle(diago(matsec)))
            #print(lecture('compress.txt'))
            #print(dediago(unrle(rle(diago(matsec)),d**2))-matsec) #petite vérfication pour voir si la compression/décompression fonctionne
                                                                  #Si c'est le cas ça devrait nous renvoyer uniquement des matrices nulles
            matsec=matsec*matquant
            #print(matsec)
            #print(transfomatrice(chemin,d)[1])
            #print(len(np.round(transfomatrice(chemin,d)*matquant)))
            #print(len(matsec))

            matsec=plus127(invdct.dot(matsec.dot(dctmat)))
            #print("127",matsec)
            #print(matsec)
            
            lmat[j]=matsec
            #transfomatrice(chemin,d)
            #print(lmat[j])
            
        #print(len(lmat))
        enreg.close()
        #transfomatrice(chemin,d,matquant,dctmat,invdct)
        mat=recoNxN(transfomatrice(chemin,d,matquant,dctmat,invdct),ligne,colonne,d)
        #print("test",mat)
        #print("final",mat)
        mat=redim(mat,ligne,colonne)
        lf.append(mat)
    matc=recoRGB(lf)
    matc=plus127(matc)
    saveIm(matc,n)
    #print(len(lecture('compress.txt')[0]))

#compDCT2('paysage.bmp',8,100)
