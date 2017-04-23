import imageio as im
import numpy as np
def recom8x8(N):#fournir le nom de l'image avant découpage, avec ".png"
    k=0;j=0
    try:
        while 1==1:#le but est d'obliger le programme a essayer des valeur de k jusqu'à que l'image demandée n'existe plus
            I=im.imread(str(N[0:N.index(".")])+"0"+str(k)+".png")
            k+=1
    except:
        k=k-1#k donne l'indice maxi horizontal
    try:
        while 1==1:
            I=im.imread(str(N[0:N.index(".")])+str(j)+"0"+".png")
            j+=1
    except:
        j=j-1#j donne l'indice maxi vertical
    print(k,j)
    for a in range(0,j+1):
        I=im.imread(str(N[0:N.index(".")])+str(a)+"0"+".png")
        if k>=1:
            for b in range(1,k+1):
                M=im.imread(str(N[0:N.index(".")])+str(a)+str(b)+".png")
                I=np.append(I,M,axis=1)#I forme un ligne de 8 pixels de haut
        if a>=1:
            A=np.append(A,I,axis=0)#regroupe les lignes de matrices /!\ pour a=0 la matrice A n'existe pas encore
        else:
            A=I#si a=0, il faut initialiser A 
    im.imsave(str(N[0:N.index(".")])+"recom.png",A)