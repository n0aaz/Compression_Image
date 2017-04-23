import imageio as im

import numpy as np
import numpy.random as alea
a=im.imread("couleurR.png")
print(a)
l=a.shape
b=np.zeros([int((l[0])/2),int((l[1])/2)])
print(b)

    
for i in range(0,int(l[0]/2)):
    for j in range(0,int(l[1]/2)):
        b[i][j]=(a[2*i][2*j] + a[2*i+1][2*j] + a[2*i][2*j+1] + a[2*i+1][2*j+1] )/4
print(b)
print(b.shape)
im.imsave("testA.png",b)

        
