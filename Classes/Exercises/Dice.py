# Name: Ahsan Khan
# Date: 10/28/20
# Description: Make a class Dice with one attribute called sides, which has a default value of 6. Write a method called roll_dice() that prints
#			   a random number between 1 and the number of the sides the dice has. Make a 6-sided diceand roll it 10 times.

from random import randint

class Dice:
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_dice(self):
		self.randNum = randint(1,6)

		for num in range(1,10):
			print(self.randNum)

dice = Dice()
dice.roll_dice()
