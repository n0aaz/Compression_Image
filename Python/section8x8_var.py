#le programme consiste a prolonger un image en recopiant la derniere ligne et la derniere colonne le nombre de fois necessaire pour obtenir un nombre de ligne et un nombre de colonnes multiples de 8. Ensuite, le programmes enregistre sous formes d'images indépendantes tous les carrés de 8x8 pixels presents dans l'image. P est le nombre de pixels par carré
import imageio as im
import numpy as np
def sec8x8(N,P):
    I=im.imread(N)
    T=I.shape;L=int(T[0]);C=int(T[1])
    Cr=C%P;Lr=L%P#savoir de combien de ligne/colonnes prolonger 
    if Cr!=0:#pas necessaire si nombre de colonnes divisible par 8
        Cr=P-Cr#donne le nombre de colonne a completer
        Cp=[]
        for k in range(0,L):
            for j in range(0,Cr):#necessité d'afficher Cr fois la meme valeur, car reshape complete lignes apres lignes
                Cp.append(I[k][C-1])#créé une liste recopiant la derniere colonne 
        Cp=np.asarray(Cp)#transforme la liste en tableau
        Cp=np.reshape(Cp,(L,Cr))#reforme une matrice de meme nombre de ligne et de nombre de colonne demandé
        I=np.append(I,Cp,axis=1)#concatene les matrice I et Cp, en ajoutant Cp au nombre de colonnes
    if Lr!=0:#pas necessaire si nombre de lignes divisible par 8
        Lr=P-Lr#donne le nombre de lignes a completer
        Lp=[]
        for k in range(0,C+Cr):
            Lp.append(I[L-1][k])#liste en reprenant les termes de la derniere ligne(comprenant ceux des nouvelles colones)
        Lp=Lp*Lr#multiplie par le nombre de listes manquantes
        Lp=np.asarray(Lp)
        Lp=np.reshape(Lp,(Lr,C+Cr))#créé une matrice de nombre de ligne necessaire et de meme nombre de colonne que I+Cp
        I=np.append(I,Lp,axis=0)
        im.imsave(str(N[0:N.index(".")]+"int.png"),I)#permet de renommer en ayant enlevé ".png" au préalable
    T=I.shape;Lf=int(T[0]);Cf=int(T[1])#reste a diviser la matrice en matrices 8x8
    for k in range(0,Lf//P):
        for j in range(0,Cf//P):#regarder chaque carré de 8x8 pixels
            M=[]
            print(k,j)
            for a in range(0,P):
                for b in range(0,P):#parcourir chaque pixel des carrés
                    M.append(I[a+k*P][b+j*P])
            M=np.asarray(M)
            M=np.reshape(M,(P,P))
            n=str(N[0:N.index(".")])+str(k)+str(j)+".png"#nom final (ayant été renommé après avoir supprimé ".png"
            im.imsave(str(n),M)