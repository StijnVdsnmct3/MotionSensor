from DbClass import DbClass
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from datetime import datetime
import os.path
import socket

camera = PiCamera()

sensor = 22
video = False
foto = True

GPIO.setmode(GPIO.BCM)
GPIO.setup (sensor, GPIO.IN)


#locaties living=1 keuken=2 gang=3
while True:
    if sensor == 1:
        beweging = True
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect('192.168.1.73', 9050)
        sock.sendall(beweging)
        ok = sock.recv(1024)
        if ok == True:
            sock.close()
        if foto == True:
            save_path = '/home/pi/flask/static/Files'
            filename = datetime.now().strftime("%Y-%m-%d %H:%M:%S.JPEG")
            complete_path = os.path.join(save_path, filename)
            camera.capture(filename)
            do = DbClass()
            do.insertlog(1,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),1,filename)
        if video == True:
            save_path = '/home/pi/flask/static/Files'
            filename = datetime.now().strftime("%Y-%m-%d %H:%M:%S.h264")
            complete_path = os.path.join(save_path, filename)
            camera.split_recording(filename)
            time.sleep(5)
            camera.stop_recording()
            do = DbClass()
            do.insertlog(1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 2, filename)

