import random
import deck


def main():
	deck1 = deck.Deck()
	deck2 = deck.Deck()

	deck1.cardList = [20,3,5,4,4,3,1,0,0,0]
	deck2.cardList = list(deck1.cardList)

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
	
	#both players draw hands in what is definitely the best way
	hand1.append(deck1.draw())
	hand1.append(deck1.draw())
	hand1.append(deck1.draw())
	hand1.append(deck1.draw())
	hand1.append(deck1.draw())
	hand1.append(deck1.draw())
	hand1.append(deck1.draw())
	hand2.append(deck2.draw())
	hand2.append(deck2.draw())
	hand2.append(deck2.draw())
	hand2.append(deck2.draw())
	hand2.append(deck2.draw())
	hand2.append(deck2.draw())
	hand2.append(deck2.draw())

	if verbosity > 0:
		print "Player 1's hand:" + str(hand1)
		print "Player 2's hand:" + str(hand2)

	turnCount = 1
	p1Life = 20
	p2Life = 20
	p1Lands = 0
	p2Lands = 0
	p1Creatures = []
	p2Creatures = []
	while p1Life > 0 and p2Life > 0:
		print "--------P1 TURN " + str(turnCount) + "--------"
		#P1 takes first turn, doesn't draw
		print "Player 1's hand:" + str(hand1)
		
		#P1 plays land if they have one
		if 0 in hand1:
			hand1.pop(hand1.index(0))
			p1Lands += 1
			print "Played a land, P1 now has " + str(p1Lands) + " lands in play"
		
		#Attacks with creatures (from last turn)
		for i in p1Creatures:
			p2Life -= i
		print "After attacks, P2 has " + str(p2Life) + " life"

		#Plays creatures in order from largest to smallest
		p1LandsTapped = 0
		landsAvailable  = p1Lands
		manaCheck = 9
		while manaCheck > 0:
			if manaCheck in hand1 and landsAvailable >= manaCheck:
				newCreature = hand1.pop(hand1.index(manaCheck))
				p1Creatures.append(newCreature)
				print "P1 Played a creature costing " + str(newCreature)
				landsAvailable -= newCreature
				
			manaCheck -=1
		print "P1's board state is " + str(p1Creatures)	

		print "--------P2 TURN " + str(turnCount) + "--------"

		#P2 takes second turn
		hand2.append(deck2.draw())
		print "Player 2's hand:" + str(hand2)
	
		#P2 plays land if they have one
		if 0 in hand2:
			hand2.pop(hand2.index(0))
			p2Lands += 1
			print "Played a land, P2 now has " + str(p2Lands) + " lands in play"
		
		#Attacks with creatures (from last turn)
		for i in p2Creatures:
			p1Life -= i
		print "After attacks, P1 has " + str(p1Life) + " life"

		#Plays creatures in order from largest to smallest
		p2LandsTapped = 0
		landsAvailable  = p2Lands
		manaCheck = 9
		while manaCheck > 0:
			if manaCheck in hand2 and landsAvailable >= manaCheck:
				newCreature = hand2.pop(hand2.index(manaCheck))
				p2Creatures.append(newCreature)
				print "P2 Played a creature costing " + str(newCreature)
				landsAvailable -= newCreature
				
			manaCheck -=1
		print "P2's board state is " + str(p2Creatures)	

		turnCount += 1
		#Allow p1 to draw a card at end of turn cycle (to account for them not drawing on first turn)	
		hand1.append(deck1.draw())



		
		
		
	
	





if __name__ == '__main__':
	main()
