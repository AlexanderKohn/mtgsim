import random


class Deck:
	"""Holds information about our deck"""

	def __init__(self):
		self.cardList = [0] * 10

	def __str__(self):
		return str(self.cardList)
	
	def shuffle(self):
		self.deck = list(self.cardList)
	#	numCards = 0
	#	for i in cardList:
	#		numCards += i
	#
	#	tempList = list(self.cardList)
	#	
	#
	#	self.deck = []
	#	while 

	def draw(self):
		numCards = 0
		for cardCount in self.deck:
			numCards += cardCount

		cardNum = random.randrange(numCards)

		cardID = 0
		while cardNum >= 0:
			cardNum -= self.deck[cardID]
			cardID += 1
		cardID -= 1
		self.deck[cardID] -= 1
		return cardID
		
		

