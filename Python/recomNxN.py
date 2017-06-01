
"""ATTENTION CETTE FONCTION A POUR ENTREE UNE LISTE DE MATRICE ET POUR SORTIE UNE MATRICE"""
def recomNxN(m):#fournir le nom de l'image avant découpage, avec ".png"
    j=m[len(m)-2]#il peut y avoir un probleme du a l'inversion des deux variables
    k=m[len(m)-1]
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
    return A