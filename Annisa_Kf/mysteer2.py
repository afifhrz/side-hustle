import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)  # Steer Right
GPIO.setup(20,GPIO.OUT)  # Steer Left
GPIO.setup(16,GPIO.OUT)  # Control
GPIO.setup(6,GPIO.OUT)   # Move Forward
GPIO.setup(26,GPIO.OUT)  # Move Backward
GPIO.setup(12,GPIO.OUT)  # Speed

def reset():
    GPIO.output(16,GPIO.LOW)
    time.sleep(1)
    GPIO.output(16,GPIO.HIGH)

    GPIO.output(20,GPIO.LOW)
    time.sleep(1)
    GPIO.output(20,GPIO.HIGH)

    GPIO.output(21,GPIO.LOW)
    time.sleep(1)
    GPIO.output(21,GPIO.HIGH)

    GPIO.cleanup()
    return

