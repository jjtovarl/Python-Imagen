"""
Obtención del histograma de una imagen RGB. Para ello se hace
uso de la librería OpenCV y, para la visualización, el paquete pyplot
de la librería matplotlib
"""
"""
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

Los parámetros de la funcióne cv2.calcHist son:
-images : es la imagen de entrada, un array numpy de tipo uint8 or float32.
-channels : el índice del canal para el cual se quiere calcular el histograma.
Se representa entre corchetes, así para una imagen ByN se da como [0]
y para una imagen RGB [0], [1], [2]
-mask : máscara de imagen. Se emplea para encontrar el histograma de
zonas concretas de la imagen, en el caso del histograma completo su valor en None
-histSize : también va entre corchetes, y representa lo que se conocen como BIN,
que determina el intervalo para el cual se quiere representar el histograma.
A escala completa seria [0,256], y en el caso que fuese [8],
sólo se necesitarían 32 valores para representar el histograma.
-ranges : Determina el RANGO, que casi siempre será [0,256].
    
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('/home/arodesc/Imágenes/IMG_4649.JPG') #carga de imagen

"""
Cuando se le una imagen en OpenCV hay que tener en cuenta que el orden de
los canales no es el habitual RGB, sino BGR.
"""
color=('b', 'g', 'r')
for i, color in enumerate(color):
    hist=cv2.calcHist(img, [i], None,[256],[0,256])
    plt.plot(hist,color) #una grafica para cada canal
    plt.xlim([0,256])   #limita el tamaño del eje
plt.show()

        
