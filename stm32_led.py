import serial
import time

ser = serial.Serial("COM4", 115200, timeout=1)

time.sleep(2)

ser.write(b'1')
print("LED ON")

time.sleep(3)

ser.write(b'0')
print("LED OFF")

ser.close()
