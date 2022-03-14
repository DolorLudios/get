import RPi.GPIO as GPIO
import time
dac=[26,19,13,6,5,11,9,10]
number=[0,1,0,1,0,1,0,1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac,number)
time.sleep(20)
GPIO.output(dac,0)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
#1 измерение
newnumber=[1,1,1,1,1,1,1,1]
GPIO.output(dac,newnumber)
time.sleep(20)
GPIO.output(dac,0)
#2 измерение
newnumber=[0,1,1,1,1,1,1,1]
GPIO.output(dac,newnumber)
time.sleep(20)
GPIO.output(dac,0)
#3 измерение
newnumber=[0,1,0,0,0,0,0,0]
GPIO.output(dac,newnumber)
time.sleep(20)
GPIO.output(dac,0)
#4 измерение
newnumber=[0,0,1,0,0,0,0,0]
GPIO.output(dac,newnumber)
time.sleep(20)
GPIO.output(dac,0)
#5 измерение
newnumber=[0,0,0,0,0,0,0,0]
GPIO.output(dac,newnumber)
time.sleep(20)
GPIO.output(dac,0)
#6 измерение
newnumber=[0,0,0,0,0,1,0,1]
GPIO.output(dac,newnumber)
time.sleep(20)
GPIO.output(dac,0)