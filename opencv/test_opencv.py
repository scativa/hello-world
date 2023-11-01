import cv2
import numpy as np

# Supongamos que tienes un array de NumPy llamado 'mi_array'
mi_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 99, 100])

# Obtener las últimas 100 posiciones del array
ultimas_100_posiciones = mi_array[-100:]

# Imprimir las últimas 100 posiciones
print(ultimas_100_posiciones)

print("Versión de OpenCV:", cv2.__version__)
