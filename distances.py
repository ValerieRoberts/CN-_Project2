import math

def calcDist(thisX, thisY, othX, othY):
	x = abs(thisX - othX)
	y = abs(thisY - othY)
	return math.sqrt(x*x + y*y)

def updatePos(x, y, xVel, yVel, time):
	newX = x + xVel*time
	newY = y + yVel*time
	return newX, newY


