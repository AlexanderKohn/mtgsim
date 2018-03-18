import random
import deck


def main():
	deck1 = deck.Deck()
	deck2 = deck.Deck()

	deck1.cardList = [20,3,5,4,4,3,1,0,0,0]
	deck2.cardList = deck1.cardList

	print deck1
	print deck2

	playGame(deck1, deck2, 1)

def playGame(deck1, deck2, verbosity=None):

	if verbosity==None:
		verbosity = 0
	
	deck1.shuffle()
	deck2.shuffle()

	hand1 = []
	hand2 = []

	if verbosity > 0:
		hand1.append(deck1.draw())
		print "Player 1's hand:" + str(hand1)

		
	
	





if __name__ == '__main__':
	main()
