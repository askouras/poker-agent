import random

cards = [[1, 'c'],[1, 'd'],[1, 'h'],[1,'s'],
		 [2, 'c'],[2, 'd'],[2, 'h'],[2,'s'],
		 [3, 'c'],[3, 'd'],[3, 'h'],[3,'s'],
		 [4, 'c'],[4, 'd'],[4, 'h'],[4,'s'],
		 [5, 'c'],[5, 'd'],[5, 'h'],[5,'s'],
		 [6, 'c'],[6, 'd'],[6, 'h'],[6,'s'],
		 [7, 'c'],[7, 'd'],[7, 'h'],[7,'s'],
		 [8, 'c'],[8, 'd'],[8, 'h'],[8,'s'],
		 [9, 'c'],[9, 'd'],[9, 'h'],[9,'s'],
		 [10, 'c'],[10, 'd'],[10, 'h'],[10,'s'],
		 [11, 'c'],[11, 'd'],[11, 'h'],[11,'s'],
		 [12, 'c'],[12, 'd'],[12, 'h'],[12,'s'],
		 [13, 'c'],[13, 'd'],[13, 'h'],[13,'s']]

hand_hierarchy = ['royal flush','straight flush','four of a kind','full house',
				  'flush','straight','three of a kind','two pair','one pair',
				  'high card']

agent_hand 		= []
player_hand  	= []

def suit(card):
	return card[1]

def value(card):
	return card[0]

def isFlush(hand):
	suits = set ()
	for card in hand:
		suits.add(suit(card))
	return len(suits) = 

def isStraight(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values.sort()
	start = values[0] - 1
	for value in values:
		if (start = 1) and (value = 14)
		if (value != start):
			return false
		else
			start = start + 1

def isSet(numberOfSame, hand):

def sets(hand):
	amounts = {
	for card in hand:



def isRoyalFlush(hand):
	if isFlush(hand):
		if isStraight(hand):

def dealHand(numberOfCards):
	return random.sample(cards, numberOfCards)

def deal(numberOfCards):
	agent_hand = dealHand(numberOfCards)
	player_hand = dealHand(numberOfCards)

def handRank(hand):
	if   isRoyalFlush(hand):
		return 0
	elif (isStraight(hand) and isFlush(hand)):
		return 1
	elif ifSet(4,hand):
		return 2
	elif 



#import random
#import itertools
#SUITS = 'cdhs'
# RANKS = '23456789TJQKA'
#DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
#hand = random.sample(DECK, 5)
#print hand
#['Kh', 'Kc', '6c', '7d', '3d']