import random
import time
import os

LEDarray = []
for i in range(30):
	LEDarray.append(0)
	

def randomNumberGenerator(max):
	while True:
		yield random.randint(0, max)
rng = randomNumberGenerator(10)

def count():
	n=0
	while True:
		yield n
		n+= 1
cnt = count()


def shift(array, shiftBy, nextValue):
	arrayLength = len(array)
	
	for i in range(arrayLength - 1):
		index = arrayLength - 2 - i
		
		array[index + 1] = array[index]
	
	array[0] = nextValue
		
	


for frame in range(1000):
	print (LEDarray)
	
	shift(LEDarray, 1, next(cnt))
	
	time.sleep(.01)
	os.system("cls")
	