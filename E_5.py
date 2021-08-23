#Paredes Márquez Carlos
#Ejercicio_5
#20 08 2021
'''Abre una imagen a color'''

import cv2
import numpy as np

im= cv2.imread('Pug.jpeg')

'''rotar 180* a lado <contrario> de la manecilla del reloj'''

im1= cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)
im2= cv2.rotate(im1, cv2.ROTATE_90_COUNTERCLOCKWISE)

'''Conviértela a escala de grises'''

R = im2[:,:,2]
G = im2[:,:,1]
B = im2[:,:,0]

ig = R*0.299 + G*0.587 + B*0.114
ig= ig.astype(np.uint8)

'''Calcula el negativo de la imagen'''

im_f = 225 - ig

'''Muestra imagen original y resultado'''

cv2.imshow('image0', im)
cv2.imshow('image1', im_f)
cv2.waitKey(0)