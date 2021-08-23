#Paredes Márquez Carlos
#Ejercicio_1
#20 08 2021
'''Abre imagen a color'''

import cv2
import numpy as np 

im= cv2.imread('Pug.jpeg')

'''Conviértela a escala de grises'''

R = im[:,:,2]
G = im[:,:,1]
B = im[:,:,0]


ig = R*0.299 + G*0.587 + B*0.114
ig= ig.astype(np.uint8)

'''Calcula el negativo de la imagen'''

im_n = 225 - ig

'''Compara ambas imagenes'''

cv2.imshow('image', im)
#cv2.imshow('image1', ig) #imagen en escala de grises
cv2.imshow('image2',im_n)
cv2.waitKey(0)