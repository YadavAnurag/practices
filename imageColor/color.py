from PIL import Image
import numpy as np 

mat = np.asarray(Image.open('pic.jpg'))

xdim = mat.shape[0]
ydim = mat.shape[1]
print(xdim,ydim)
for i in range(xdim):
	for j in range(ydim):
		pixel = mat.item(i,j)
		print(pixel,' at ', (i,j))