import random

# The possible suits and card values
suits = ['c','d','h','s']
vals  = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# Where player[0] is the agent
players = []
# Keeps track of previous hands
knowledgeBaseHands = []
# How much money each player has
players_money = []
# Amount of money in the pot
pot = 0
# The cards in the deck
deck = []
# Keeps track of who folded
inHand = []
# Keeps track of who's still playing
inGame = []
# Keeps track of what each player did in the hand
actions = []
# Keeps track of previous moves
knowledgeBaseActions = []
# Track the payout
result = []
# Keeps track of previous payouts
knowledgeBasePayouts = []

# Create deck by combining suits and vals and adding to a list
def fillDeck():
	for suit in suits:
		for val in vals:
			deck.append([val,suit])

# Add players to be dealth into game
def addPlayers(numberOfPlayers):
	for i in range(numberOfPlayers):
		players.append([])

def addPlayersStart(numberP):
	for i in range(numberP):
		players_money.append(100)
		inHand.append(True)
		inGame.append(True)

# Shuffle the deck
def shuffle():
	random.shuffle(deck)

# Deal to each player
def deal(numberOfCards):
	for i in range(numberOfCards):
		for player in players:
			player.append(deck.pop())

# All players ante up (add ante to the pot)
def ante():
	global players_money
	global pot
	players_money = [player_money - 10 for player_money in players_money]
	for player_money in players_money:
		pot += 10
		player_money -= 10
	print "All players have added 10 credits to the pot for the ante"

# Player raise
def raised(player_index):
	global pot
	global players_money
	global actions
	pot += 10
	players_money[player_index] -= 10
	actions.insert(player_index,'raised')
	print "Player " + str(player_index) + " has raised"

# Remove players from list if they have run out of money
def checkPlayers():
	global players_money
	global inGame
	global players
	outPlayers = []
	counter = 0
	while counter < len(players_money):
		if players_money[counter] == 0:
			outPlayers.append(counter)
		counter += 1
	counter2 = 0
	while counter2 < len(outPlayers):
		inGame[outPlayers[counter2]] = False
		counter += 1

# If agent raises (after opponents stayed), force opponents to raise or fold
def forceResponse():
	global actions

# Start opponent(s)
def startOpponent(index):
	global actions
	rank = handRank(players[index])
	# Raise if hand is a straight or better
	if rank < 6:
		raised(index)
	else:
		actions.insert(index,'stayed')
		print "Player " + str(index) + " has stayed"

def startAgent():
	global actions
	index = 0
	rank = handRank(players[index])
	# Did the opponents raise?
	if 'raised' in actions:
		# Agent has better than a pair, raise
		if rank < 8:
			raised(index)
		# Otherwise stay/fold
		else:
			actions.insert(index,'stayed')
			inHand[index] = False
			print "Player " + str(index) + " has folded"
	else:
		if rank < 6:
			raised(index)
			inHand[1] = False
		else:
			print "Player " + str(index) + " has stayed"

def remember():
	knowledgeBaseActions.append(actions)

def startGame():
	addPlayersStart(2)
	while not gameOver():
		startHand()
	if gameOver():
		whoWonGame()

# Setup deck and deal hands to each player
def startHand():
	global actions
	global players
	global deck
	global pot
	actions = []
	players = []
	deck = []
	pot = 0
	addPlayers(2)
	checkPlayers()
	fillDeck()
	shuffle()
	ante()
	deal(5)
	startOpponent(1)
	startAgent()
	whoWon()
	remember()
	print players_money

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

# Sort cards by card rank
def sortCards(values):
	vals = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	ranks = []
	for value in values:
		ranks.append(vals.index(value))
		ranks.sort()
	sortedValues = []
	for rank in ranks:
		sortedValues.append(vals[rank])
	return sortedValues

# Determine if given hand is a flush (all have the same suit)
def isFlush(hand):
	suits = set ()
	for card in hand:
		suits.add(suit(card))
	return len(suits) == 1

# Determine if given hand is a straight (a run of 5)
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
	if isStraight(hand) and isFlush(hand):
		values = []
		for card in hand:
			values.append(value(card))
		values = sortCards(values)
		return values

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

# Determine if given hand has a set of given size 
#  (if first argument is 2, will return true if the hand has a pair)
def hasSet(numberOfSame, hand):
	if (numberOfSame in sets(hand)):
		return True

# Determine if given hand contains two pairs (i.e. [2,2,6,7,7])
def hasTwoPair(hand):
	setses = sets(hand)
	pairs = 0
	for setse in setses:
		if setse == 2:
			pairs += 1
	return pairs == 2

# Determine the hand's high card
def highCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-1]

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
	else:
		return 9 # later will find out what the high card is (when needed)

def whoWon():
	global pot
	player_ranks = []
	for player in players:
		player_ranks.append(handRank(player))
	bestHand = min(player_ranks)
	playersWithBestHand = []
	counter = 0
	while counter < len(player_ranks):
		if player_ranks[counter] == bestHand:
			playersWithBestHand.append(counter)
		counter += 1
	payOut = pot/len(playersWithBestHand)
	for player in playersWithBestHand:
		players_money[player] += payOut

# Figure out is over, if over, print winner
def gameOver():
	checkPlayers()
	playersLeft = 0
	for True in inGame:
		playersLeft += 1
	if playersLeft == 1:
		return True
	else:
		return False

def whoWonGame():
	playersLeft = 0
	for True in inGame:
		playersLeft += 1
		print playersLeft
	if playersLeft == 1:
		winner = inGame.index(True)
		print "Player " + str(winner) + " has won the game with " + str(players_money[winner]) + " credits"

startGame()