"""Module du programme 'comp_dct_2.py' """
import imageio as im
import numpy as np
np.set_printoptions(precision=5)#permet de ne pas avoir de chiffres en écriture décimale trop long
np.set_printoptions(suppress=True)#autorise la suppression automatique d'éléments du tableau(?)
##matrice DCT
def matDCT(n):
    import math as m
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
##linéarisation en serpent de la matrice
def diago(l):
	m,n=np.shape(l)[0],np.shape(l)[1]
	if m != n :
		return False
		
	a,b=[],[]
	for i in range(m):
		for k in range (i+1):
			if i%2==0:
				a.append(l[k][i-k])
				if i!=m-1:
					b.append(l[m-1-k][m-1-(i-k)])
			else:
				a.append(l[i-k][k])
				if i!=m-1:
					b.append(l[m-1-(i-k)][m-1-k])	
	b.reverse()			
	return (a+b)

##lecture image
def lectImage(n):
    return np.asarray(im.imread(n))
##moins 127
def moins127(n):
    return n-127
##decomp image couleur
def decomCouleur(i):
    t=i.shape;n=t[2];c=t[1];l=[t];ligne=t[0]
    a=np.split(i,n,axis=2)#retourne un liste des matrices de chaque dimension
    for k in range(n):
        l.append(np.reshape(a[k],(ligne,c)))#redonne la forme de matrices 8x8
    return l
##rajout de lignes et colonnes identiques pour obtenir un multiple de N
def retail(i,n):
    t=i.shape;l=t[0];c=t[1];lc=0;cc=0
    if l%n!=0:
        lc=n-l%n#nombre de lignes à compléter
    if c%n!=0:
        cc=n-c%n#nombre de colonnes à compléter
    for k in range(lc):
        i=np.append(i,i[l-1:l,:],axis=0)
    for k in range(cc):
        i=np.append(i,i[:,c-1:c],axis=1)
    return i
##decomposition en carré de NxN
def decoupNxN(i,n):
    t=i.shape;l=t[0];c=t[1]
    liste=[]
    for k in range(l//n):
        for j in range(c//n):
            liste.append(i[k*n:(k+1)*n,j*n:(j+1)*n])
    return liste
##matrice de quantification
def quantMat(quant):
    q=[800,600,500,800,1200,2000,2550,2550],[550,600,700,950,1300,2550,2550,2550],[700,650,800,1200,2000,2550,2550,2550],[700,850,1100,1450,2550,2550,2550,2550],[900,1100,1850,2550,2550,2550,2550,2550],[1200,1750,2550,2550,2550,2550,2550,2550],[2450,2550,2550,2550,2550,2550,2550,2550],[2550,2550,2550,2550,2550,2550,2550,2550]
    q=0.1*np.asarray(q)
    q=np.reshape(q,(8,8))
    if quant!=0:
        q=np.ceil(q/quant)
    return q
##recomposition de la matrice image
def recoNxN(i,ligne,colonne,d):
    taillel=ligne//d
    taillec=colonne//d
    if ligne%d!=0:#definition de la taille de la matrice a reconstituer
        taillel=taillel+1
    if colonne%d!=0:
        taillec=taillec+1
    for k in range(taillel):
        a=i[k*taillec]
        for j in range(1,taillec):
            a=np.append(a,i[k*taillec+j],axis=1)
        if k==0:
            mat=a
        else:
            mat=np.append(mat,a,axis=0)
    return mat
##redimensionnage
def redim(i,ligne,colonne):
    i=i[0:ligne,0:colonne]
    return i
##recomposition RGB
def recoRGB(i):
    l=np.stack(i,axis=2)
    return l
##plus 127
def plus127(i):
    return i+127
##sauvegarde image
def saveIm(i,n):
    n=n[0:n.index(".")]+"comp.bmp"
    im.imsave(n,i)
