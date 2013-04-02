import random

# The possible suits and card values
suits = ['c','d','h','s']
vals  = ['2,','3','4','5','6','7','8','9','10','J','Q','K','A']

# Where player[0] is the agent
players = []

players_money = []

pot = 0

# Create deck by combining suits and vals and adding to a list
def fillDeck():
	deck = []
	for suit in suits:
		for val in vals:
			deck.append([val,suit])
	return deck

# Add players to be dealth into game
def addPlayers(numberOfPlayers):
	for i  in range(numberOfPlayers):
		players.append([])
		players_money.append(100)

# Deal to each player
def deal(numberOfCards):
	for i in range(numberOfCards):
		for player in players
			player.append(deck.pop())

# All players ante up (add ante to the pot)
def ante():
	for player_money in players_money:
		player_money -= 5
		pot += 5

# Setup deck and deal hands to each player
def startGame():
	deck = fillDeck()
	shuffle(deck)
	addPlayers(2)
	ante()
	deal(5)

# Get the suit of a given card
def suit(card):
	return card[1]

# Get the value of a given card
def value(card):
	return card[0]

# Determine the hand's low card
def lowCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[0]

# Sort cards by card rank -- I'm working on it
def sortCards(values):
	vals = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	ranks = []
	for value in values:
		ranks.append(vals.index(value))
		ranks.sort()
	sortedValues = []
	for rank in ranks:
		sortedValues.append(vals[rank])
	return sortedValues]

# Determine if given hand is a flush (all have the same suit)
def isFlush(hand):
"""
	amountsSuits = {}
	for suit in suits:
		amountsSuits[suit] = 0
	for card in hand:
		amountsSuits[suit(card)] = amountsSuits[suit(card)] + 1
	flushSets = []
	for item in amountsSuits:
		flushSets.append(amountsSuits[item])
	flushSets.sort()
	return 5 in flushSets
"""
	suits = set ()
	for card in hand:
		suits.add(suit(card))
	return len(suits) = 1


# Determine if given hand is a straight (a run of 5)
"""
def isStraight(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)

	low = lowCard(hand)

	start = values[0] - 1
	for value in values:
		if value != start + 1:

		if (start = 1) and (value = 14)
		if (value != start):
			return false
		else
			start = start + 1
"""

def isStraight(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	
	if (('A' in values) and ('2' in values) and ('3' in values)
	and ('4' in values) and ('5' in values)):
		return True
	else:
		low = vals.index(lowCard(hand))
		rangeUp = range(low,low + 5)
		ranks = []
		for val in values:
			ranks.append(vals.index(val))
		ranks.sort()
		return ranks == rangeUp

# Determine if given hand is a royal flush (suited [10,J,Q,K,A])
def isRoyalFlush(hand):
	return isStraightFlush(hand) and (lowCard(hand) is '10')

# Determine if given hand is both a straight and a flush
def isStraightFlush(hand):
	return isStraight(hand) and isFlush(hand)

# Determine if given hand has a set of given size 
#  (if first argument is 2, will return true if the hand has a pair)
def hasSet(numberOfSame, hand):
	if (numberOfSame in sets(hand)):
		return true

# Determine if given hand contains two pairs (i.e. [2,2,6,7,7])
def hasTwoPair(hand):
	setses = sets(hand)
	pairs = 0
	for setse in setses:
		if setse = 2
			pairs += 1
	return pairs = 2

# Determine the hand's high card
def highCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-1]

# Find the sets of a hand and return a sorted list with the number of 
#   occurances of each card
def sets(hand):
	amountsVals = {}
	for val in vals:
		amountsVals[val] = 0
	for card in hand:
		amountsVals[value(card)] += 1
	valueSets = []
	for item in amountsVals:
		valueSets.append(amountsVals[item])
	valueSets.sort()
	return valueSets

# Shuffle the deck
def shuffle():
	random.shuffle(cards)

# Get the rank of the hand (a lower number is a better hand)
def handRank(hand):
	if   isRoyalFlush(hand):
		return 0
	elif isStraightFlush(hand):
		return 1
	elif hasSet(4,hand):
		return 2
	elif (hasSet(3,hand) and hasSet(2,hand)):
		return 3
	elif  isFlush(hand):
		return 4
	elif isStraight(hand):
		return 5
	elif hasSet(3,hand):
		return 6
	elif hasTwoPair(hand):
		return 7
	elif hasSet(2,hand):
		return 8
	else return 9 # later will find out what the high card is (when needed)

def whoWon():
	player_ranks = []
	for player in players:
		player_ranks.append(handRank(player))

def gameOver():