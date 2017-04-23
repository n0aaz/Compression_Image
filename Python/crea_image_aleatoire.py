#/!\ mettre en mémoire au préalable la fonction creamat, qui se trouve dans le fichier crea_matrice_alea.py
import imageio as im
def creaim(L,C,Name):
    M=creamat(L,C)
    im.imsave(str(Name),M)