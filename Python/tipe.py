"""Pour pouvoir utiliser ce ficher comme un module, il faut, soit le placer au même endroit que le reste des modules utilisés par python (info a vérifier quand même), sinon definir le nouveau répertoire de travail dans lequel se trouve ce ficher grâce à la commande os.chdir('emplacement').
Il suffit ensuite d'appeler n'importe quelle fonction du module par 'from tipe import __' ou importer la module, par exemple 'import tipe as t'.
Une fois importée la commande 'help(tipe)' permet de connaître les noms des matrices présentes"""

import numpy.random as rd
import numpy as np
import imageio as im
import os as os

## Fonction de décomposition d'une image couleur en trois images RGB

"""ATTENTION IMAGES ACTUELLEMENT SAUVEGARDEES SOUS FORME D'IMAGES, ET NON PAS SOUS FORME DE MATRICES!!!"""
def RGBdecom(Nom_entree,Nom_sortie):#Name1=nom entrée, Name2=nom de sortie
    Name1=Nom_entree
    Name2=Nom_sortie
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

## Fonction de recomposition d'une image couleur a partir de trois images en noir et blanc(rouge,verte,bleue)

"""ATTENTION, CETTE FONCTION TRAITE DES IMAGES EN ENTREE ET DES IMAGES EN SORTIE, PAS DES MATRICES!!!"""
def RGBrecom(Nom_entree,Nom_sortie):#ATTENTION: N1=image RGB, sans precision couleur ni extension,MAIS N2 a donner avec extension
    N2=Nom_sortie
    N1=Nom_entree
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
    
## Fonction de décomposition d'une matrice en matrices carrées de 8x8

#le programme consiste a prolonger un image en recopiant la derniere ligne et la derniere colonne le nombre de fois necessaire pour obtenir un nombre de ligne et un nombre de colonnes multiples de 8. Ensuite, le programmes enregistre sous formes d'images indépendantes tous les carrés de 8x8 pixels presents dans l'image.

#RETOURNE UNE LISTE DE MATRICES

def Sec8x8(Nom_image):
    N=Nom_image
    I=im.imread(N)
    T=I.shape;L=int(T[0]);C=int(T[1])
    Cr=C%8;Lr=L%8						#savoir de combien de ligne/colonnes prolonger 
    if Cr!=0:							#pas necessaire si nombre de colonnes divisible par 8
        Cr=8-Cr							#donne le nombre de colonne a completer
        Cp=[]
        for k in range(0,L):
            for j in range(0,Cr):		#necessité d'afficher Cr fois la meme valeur, car reshape complete lignes apres lignes
                Cp.append(I[k][C-1])	#créé une liste recopiant la derniere colonne 
        Cp=np.asarray(Cp)				#transforme la liste en tableau
        Cp=np.reshape(Cp,(L,Cr))		#reforme une matrice de meme nombre de ligne et de nombre de colonne demandé
        I=np.append(I,Cp,axis=1)		#concatene les matrice I et Cp, en ajoutant Cp au nombre de colonnes
    if Lr!=0:							#pas necessaire si nombre de lignes divisible par 8
        Lr=8-Lr							#donne le nombre de lignes a completer
        Lp=[]
        for k in range(0,C+Cr):
            Lp.append(I[L-1][k])		#liste en reprenant les termes de la derniere ligne(comprenant ceux des nouvelles colones)
        Lp=Lp*Lr						#multiplie par le nombre de listes manquantes
        Lp=np.asarray(Lp)
        Lp=np.reshape(Lp,(Lr,C+Cr))		#créé une matrice de nombre de ligne necessaire et de meme nombre de colonne que I+Cp
        I=np.append(I,Lp,axis=0)
        im.imsave(str(N[0:N.index(".")]+"int.png"),I)#permet de renommer en ayant enlevé ".png" au préalable
    T=I.shape;Lf=int(T[0]);Cf=int(T[1])	#reste a diviser la matrice en matrices 8x8
    liste=[]
    for k in range(0,Lf//8):
        for j in range(0,Cf//8):		#regarder chaque carré de 8x8 pixels
            M=[]
            for a in range(0,8):
                for b in range(0,8):	#parcourir chaque pixel des carrés
                    M.append(I[a+k*8][b+j*8])
            M=np.asarray(M)
            M=np.reshape(M,(8,8))
            n=str(N[0:N.index(".")])+str(k)+str(j)+".png"#nom final (ayant été renommé après avoir supprimé ".png"
            #im.imsave(str(n),M)
            liste.append(M)
    return liste
    
## Fonction de décomposition d'une matrice carrée en matrices de taille désirée

"""ATTENTION CETTE FONCTION PREND COMME SOURCE UNE IMAGE ET RETOURNE DES IMAGES (A MODIFIER DANS LE PROGRAMME FINAL)!!!"""
def SecNxN(Nom_image,Taille):
    P=Taille
    N=Nom_image
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
            
## Fonction de recomposition d'une image a partir de toutes les images de taille 8x8 extraites

"""ATTENTION CETTE FONCTION A POUR ENTREE DES IMAGES ET POUR SORTIE UNE AUTRE IMAGE"""
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
            
## Fonction de création d'une matrice aléatoire en 2D

def CreaMat2D(Lignes,Colonnes):
    L=Lignes
    C=Colonnes
    a=rd.random_integers(0,255,L*C)
    M=[]
    for k in range(0,L*C):
        m=(a[k])
        M.append(m)
    #print(len(M))
    M=np.asarray(M)
    #print(len(M))
    M=np.reshape(M,(L,C))
    return M
    
## Fonction de création d'une matrice aléatoire en 3D

def CreaMat3D(Lignes,Colonnes):
    L=Lignes
    C=Colonnes
    a=rd.random_integers(0,255,L*C)#liste aléatoire destinée a la couleur rouge
    b=rd.random_integers(0,255,L*C)#liste aléatoire destinée a la couleur verte
    c=rd.random_integers(0,255,L*C)#liste aléatoire destinée a la couleur bleue
    M=[]
    for k in range(0,L*C):
        m=(a[k],b[k],c[k])#création d'une liste des valeurs des trois couleurs pour chaque pixel
        M.append(m)#ajouter cette liste a un autre liste qui constituera la matrice
    #print(len(M))
    M=np.asarray(M)#transforme la liste en un tableau uniligne
    #print(len(M))
    M=np.reshape(M,(L,C,3))#trnasforme ce tableau uniligne en une marice de L lignes, C colonnes et 3 couleurs
    return M
    
## Fonction permettant la création d'une image aléatoire en couleur

#/!\ mettre en mémoire au préalable la fonction creamat, qui se trouve dans le fichier crea_matrice_alea.py
import imageio as im
def creaim(Lignes,Colonnes,Nom_sortie):
    L=Lignes
    C=Colonnes
    N=Nom_sortie
    M=CreaMat3D(L,C)
    im.imsave(str(Name),M)
    
## Fonction de multiplication de matrices

def MultMat(A,B):
	matrice=[]
	for i in range(len(A)):
		ligne=[]
		for j in range(len(B)):
			som=0
			for k in range(len(A)):
				som+=A[i][k]*B[k][j]
			ligne.append(som)
		matrice.append(ligne)
		
## Fonction de création de la matrice de la DCT

def c(x):
	if x==0 :
		return 1/m.sqrt(2)
	elif x>0 :
		return 1
		
def MatDCT(n):
	matrice=[]
	for i in range(n):
		ligne=[]
		for j in range(n):
			if i==0 : 
				ligne.append(1/m.sqrt(n))
			else:
				ligne.append(m.sqrt(2/n)*m.cos(((2*j+1)*i*m.pi)/(2*n)))
		matrice.append(ligne)
	return np.asarray(matrice)
				
#print(MatDCT(8))

## Fonction d'inversion d'une matrice

"""/!\ ATTENTION PAS DE SECURITE SI MATRICE NON INVERSIBLE !!!"""
np.set_printoptions(precision=5)#permet de ne pas avoir de chiffres en écriture décimale trop long
np.set_printoptions(suppress=True)#autorise la suppression automatique d'éléments du tableau(?)
def InvMat(Matrice):
    M=Matrice
    T=M.shape;L=int(T[0])
    I=np.zeros([L,L])# création matrice identité
    for k in range(0,L):
        I[k][k]=1
    #print(I)
    M=np.append(M,I,axis=1)#colle les matrices M et I
    print('1',M)
    for k in range(0,L-1):#création d'une matrice triangulaire supérieure
        for j in range(k+1,L):
            if M[k][k]!=0:#vérifier que le coef de la diagonale est différent de 0, sinon division par 0!
                A=M[j][k]/M[k][k]#permet d'appliquer le pivot de gauss
                for l in range(0,2*L):
                    M[j][l]=M[j][l]-A*M[k][l]#prolonge le calcul sur toute la ligne
    #print('2',M)
    for k in range(1,L):#création de la matrice diagonale
        for j in range(0,k):
            if M[k][k]!=0:#vérifier que le coef de la diagonale est différent de 0, sinon division par 0!
                A=M[j][k]/M[k][k]#permet d'appliquer le pivot de gauss en remontant
                for l in range(0,2*L):
                    M[j][l]=M[j][l]-A*M[k][l]#prologe le calcul sur toute la ligne
    #print('3',M)
    for k in range(0,L):
        A=M[k][k]
        for l in range(0,2*L):
            M[k][l]=M[k][l]/A#divise la ligne par la valeur du coefficient de la diagonale
    #print('4',M)
    for k in range(L-1,-1,-1):#/!\ si range(0,L) une ligne sur deux sera supprimée
        M=np.delete(M,(k),axis=1)#permet de supprimer la k-ème colonne de M, et donc de retourner l'inverse de M
    return M