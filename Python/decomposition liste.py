import imageio as im
import numpy as np
def RGBdecoml(Name1,Name2):#Name1=nom entrée, Name2=nom de sortie
    R=Name2+"R.png"#Noms complets de fichiers de sortie
    G=Name2+"G.png"
    B=Name2+"B.png"
    I=im.imread(Name1)
    T=I.shape#Taille de l'image
    L=T[0]
    l=T[1]
    r=[];g=[];b=[]
    print(L,l)
    for k in range(0,L):
        for j in range(0,l):
            r.append(int(tuple(I[k][j])[0]))
            g.append(int(tuple(I[k][j])[1]))
            b.append(int(tuple(I[k][j])[2]))
            print(k)
    r=np.asarray(r)
    g=np.asarray(g)
    b=np.asarray(b)
    r=np.reshape(r,(L,l))#permet de redonner une dimension de matrice (L,l) à une matrice ligne
    g=np.reshape(g,(L,l))
    b=np.reshape(b,(L,l))
    im.imsave(str(R),r)
    im.imsave(str(G),g)
    im.imsave(str(B),b)
    print("Conversion effectuée avec succès")
#400*600=240000pixels -> 3minutes 41 secondes