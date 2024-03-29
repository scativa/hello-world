import cv2
import numpy as np
import random
import pygame
# import simpleaudio as sa

# Definir el umbral para activar la alerta de sonido
umbral = 0.9

# Cargar el archivo de sonido
# wave_obj = sa.WaveObject.from_wave_file("alert.wav")  
# Inicializar pygame y cargar el sonido
pygame.init()
alert_sound = pygame.mixer.Sound("./opencv/sonido_err.wav")  # Reemplaza "alert.wav" con el nombre de tu archivo de sonido
alert_ok = pygame.mixer.Sound("./opencv/sonido_ok.wav")  # Reemplaza "alert.wav" con el nombre de tu archivo de sonido

# Crear una ventana de OpenCV
window_name = "Función en vivo"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)

# # Función que calcula los valores de la función
# def calcular_funcion(x):
#     # resultado = np.array([random.randint(0, 100) for _ in range(len(x))])
#     # return resultado
#     # random.randint(10,90)  # Cambia esta función según tus necesidades
#     nuevo_elemento = x[-1] + 1
#     x = np.append(x, nuevo_elemento)
#     return x


# Rango de valores de x
x_values = np.arange(0, 1, 1)
y_values = np.arange(0, 1, 1)

# Función para verificar el umbral y reproducir el sonido
def check_umbral(x, umbral):
    if x > umbral:
        alert_sound.play()
        # play_obj = wave_obj.play()
        # play_obj.wait_done()
    else:
        alert_ok.play()

while True:
    # Crear una imagen en blanco
    image = np.zeros((700, 900, 3), dtype=np.uint8)
    
    # Calcular los valores de la función y trazarlos en la imagen
    
    nuevo_valor = random.randint(0,101)
    x_values = np.append(x_values, x_values[-1] + 1)[:100]
    y_values = np.append(y_values, nuevo_valor)[-100:]

    gy_values = (y_values / 100) * 600  # Escala los valores para que se ajusten a la ventana
    points = np.column_stack((x_values, gy_values)).astype(np.int32)
    cv2.polylines(image, [points], isClosed=False, color=(0, 255, 50), thickness=2)

    # Mostrar la imagen en la ventana
    cv2.imshow(window_name, image)

    check_umbral(nuevo_valor,80)

    # Esperar por una tecla y salir si se presiona la tecla 'q'
    key = cv2.waitKey(3)
    if key == ord('q'):
        break


# Cerrar la ventana y liberar recursos
cv2.destroyWindow(window_name)


