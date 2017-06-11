import numpy as np
import os as os
#quant,poids par couleur,poids total,taux de compression
#quant=liste des valeurs de quantification a tester pour le tableau
#pour ouvrir un tableau deja enregistrer, il faut utiliser "np.load('nomfichier.npy')"
def tabpoids(nom,quant,sortie):
    tab=np.zeros((len(quant),6))
    poids=os.path.getsize(nom)
    for k in range(len(quant)):
        compDCT2(nom,8,quant[k])
        tab[k][0]=quant[k]
        tab[k][1]=os.path.getsize("1.txt")
        tab[k][2]=os.path.getsize("2.txt")
        tab[k][3]=os.path.getsize("3.txt")
        tab[k][4]=tab[k][3]+tab[k][2]+tab[k][1]
        tab[k][5]=poids/tab[k][4]
    np.save(sortie,tab)
    print(poids,tab)