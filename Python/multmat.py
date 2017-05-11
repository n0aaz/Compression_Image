def multmat(A,B):
	matrice=[]
	for i in range(len(A)):
		ligne=[]
		for j in range(len(B)):
			som=0
			for k in range(len(A)):
				som+=A[i][k]*B[k][j]
			ligne.append(som)
		matrice.append(ligne)
