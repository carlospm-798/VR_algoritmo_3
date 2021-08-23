#Paredes Márquez Carlos
#Ejercicio_2
#20 08 2021
'''Abre una imagen a color'''
import cv2
import numpy as np

im = cv2.imread('Pug.jpeg')

'''Calcula el negativo de la imagen'''

im_n = 225 - im

"""Muestra las dos imágenes, original y resultado"""

cv2.imshow('image0', im)
cv2.imshow('image1', im_n)
cv2.waitKey(0)