import random
import time

msg_inc = 0
while True:
    msg_random = random.randint(0, 10)
    mensaje = f"Inc={msg_inc:05d} - Random={msg_random:02d}"
    print(mensaje)
    msg_inc += 1

    time.sleep(0.6)




