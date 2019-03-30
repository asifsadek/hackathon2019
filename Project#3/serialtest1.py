import serial
import time
# [   31.231234] cdc_acm 1-1.2:1.0: ttyACM0: USB ACM device

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600
)

time.sleep(1)

def blink():
	ser.write('o'.encode())
	time.sleep(1)
	ser.write('s'.encode())
	time.sleep(1)

while 1:
	blink()

# blink()


# SERIAL TEST SUCCESSFULL
