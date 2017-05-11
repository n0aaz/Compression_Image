import math as m
import numpy as np

def c(x):
	if x==0 :
		return 1/m.sqrt(2)
	elif x>0 :
		return 1
		
def matdct(n):
	matrice=[]
	for i in range(n):
		ligne=[]
		for j in range(n):
			if i==0 : 
				ligne.append(1/m.sqrt(n))
			else:
				ligne.append(m.sqrt(2/n)*m.cos(((2*j+1)*i*m.pi)/(2*n)))
		matrice.append(ligne)
	return matrice
				
matdct(8)
