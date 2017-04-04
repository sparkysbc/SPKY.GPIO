import SPKY.GPIO as GPIO

validPins = [11,18,23,24]

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.OUT)

for pin in validPins:
	fun = GPIO.gpio_function(pin)
	print fun
