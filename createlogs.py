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
GPIO.setup(sensor, GPIO.IN)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.99', 9050))


def motion(video, foto):
    if foto == True:
        save_path = "/home/pi/project1/static/Files/"
        filename = datetime.now().strftime("%Y-%m-%d_%H:%M:%S.jpg")
        complete_path = os.path.join(save_path, filename)
        camera.capture(complete_path)
        print("nu database")
        do = DbClass()
        do.insertlog(1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1, filename)
    if video == True:
        save_path = "/home/pi/project1/static/Files/"
        filename = datetime.now().strftime("%Y-%m-%d_%H:%M:%S.h264")
        complete_path = os.path.join(save_path, filename)
        camera.start_recording(complete_path)
        camera.wait_recording(5)
        camera.stop_recording()
        do = DbClass()
        do.insertlog(1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 2, filename)

#locaties living=1 keuken=2 gang=3
while True:
    try:
        #check voor beweging
        GPIO.wait_for_edge(sensor, GPIO.RISING)
        data = 'beweging'
        sock.sendall(data.encode('utf-8'))
        motion(video,foto)
        time.sleep(10)
    except:
        camera.close()
        GPIO.cleanup()
