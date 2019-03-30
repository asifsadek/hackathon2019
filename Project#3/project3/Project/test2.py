import time
import serial

ser = serial.Serial("COM5", 9600)

ser.write('o')