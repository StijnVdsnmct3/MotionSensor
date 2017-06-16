import socket
import RPi.GPIO as GPIO
import time

import RPi.GPIO as GPIO
import time





class LCD:

    def __init__(self, RS, E, D4, D5, D6, D7):
        self.__RS = RS
        self.__E = E
        self.__D4 = D4
        self.__D5 = D5
        self.__D6 = D6
        self.__D7 = D7
        self.__lijstpinnen = [self.__D7, self.__D6, self.__D5,self.__D4]


        self.__setup()

    def __setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__RS, GPIO.OUT)
        GPIO.setup(self.__E, GPIO.OUT)
        for i in range(4):
            GPIO.setup(self.__lijstpinnen[i], GPIO.OUT)

    def init(self):
        self.__manualreset()
        self.clear_display(0x01)

    def function_set(self, data):
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()
        time.sleep(0.1)
        data = data << 4
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()
        time.sleep(0.1)

    def display_on(self, data):
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()
        time.sleep(0.1)
        data = data << 4
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()
        time.sleep(0.1)

    def display_of(self, data):
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()
        time.sleep(1)
        data = data << 4
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()

    def clear_display(self, data):
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()
        data = data << 4
        self.eHoogInstructie()
        self.setGPIODataBits(data)
        self.eLaagInstructie()
        time.sleep(0.005)

    def eHoogData(self):
        GPIO.output(self.__E, GPIO.HIGH)
        GPIO.output(self.__RS, GPIO.HIGH)

    def eLaagData(self):
        GPIO.output(self.__E, GPIO.LOW)
        GPIO.output(self.__RS, GPIO.HIGH)

    def eHoogInstructie(self):
        GPIO.output(self.__E, GPIO.HIGH)
        GPIO.output(self.__RS, GPIO.LOW)

    def eLaagInstructie(self):
        GPIO.output(self.__E, GPIO.LOW)
        GPIO.output(self.__E, GPIO.LOW)

    def setGPIODataBits(self, data):
        filter = 0x80
        for i in range(4):
            resultaat = data & filter
            if resultaat == 0:
                GPIO.output(self.__lijstpinnen[i], GPIO.LOW)
            else:
                GPIO.output(self.__lijstpinnen[i], GPIO.HIGH)
            data = data << 1

    def sendstring(self, data):
        i = 0
        while i < len(data):
            ascii = ord(data[i])
            self.eHoogData()
            self.setGPIODataBits(ascii)
            self.eLaagData()
            time.sleep(0.1)
            ascii = ascii << 4
            self.eHoogData()
            self.setGPIODataBits(ascii)
            self.eLaagData()
            i += 1
            time.sleep(0.1)

    def __manualreset(self):
        time.sleep(0.11)
        self.eHoogInstructie()
        self.setGPIODataBits(0x30)
        self.eLaagInstructie()
        time.sleep(0.005)
        self.eHoogInstructie()
        self.setGPIODataBits(0x30)
        self.eLaagInstructie()
        time.sleep(0.0002)
        self.eHoogInstructie()
        self.setGPIODataBits(0x30)
        self.eLaagInstructie()
        time.sleep(0.0002)
        self.eHoogInstructie()
        self.setGPIODataBits(0x20)
        self.eLaagInstructie()
        time.sleep(0.0002)
        self.function_set(0x28)
        self.display_of(0x08)
        self.clear_display(0x01)
        self.display_on(0x0F)

led = 13
button = 16
scherm = LCD(17,27,19,26,21,22)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.99', 9050))
sock.listen(1)
connection, address = sock.accept()

main()


while True:
    try:
        knop = GPIO.input(button)
        scherm.init()
        scherm.sendstring('HomeSecurity V1')



        beweging = connection.recv(1024).decode()

        if beweging == 'beweging':
            while knop == 1:
                print("ik zit lus")
                scherm.init()
                GPIO.output(led, GPIO.HIGH)
                scherm.sendstring('BEWEGING!!!!!')
                time.sleep(5)
                knop = GPIO.input(button)
        GPIO.output(led, GPIO.LOW)
        scherm.init()
        scherm.sendstring('U Bent Alert')
        time.sleep(2)
    except:
        connection.close()
        GPIO.cleanup()

