# 1. Importar el módulo tello de la librería djitellopy
from djitellopy import tello

# 2. Crear una instancia del objeto Tello
drone = tello.Tello()

# 3. Establecer una conexión con el dron. Recordar que hay que conectarse a la WiFi del dron.
drone.connect()

# 4. Enviar el comando de despegue.
drone.takeoff()

# 5. Hacer algo con el dron. Enviar un comando para que rote 360 grados
drone.rotate_clockwise(360)

# 6. Enviar el comando de aterrizaje
drone.land()

# 7. Terminar la ejecución
drone.end()
