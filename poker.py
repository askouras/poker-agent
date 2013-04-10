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
# Holds the actions the opponent makes - raise or stay
opponentHistory = []
# Holds the [[agents hand rank], [agents play], [opponents play]]
agentHistory =[[],[],[]]

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

"""
#Raise function
def raiseAmount(10):
    global players_money
    global pot
    players_money = [player_money - 10 for player_money in players_money]
    for player_money in players_money:
        pot += 10
            player_money -= 10
return "raise"
"""

#************ to stay ************#
def stay():
    global players_money
    global pot
    players_money = [player_money - 0 for player_money in players_money]
    for player_money in players_money:
        pot += 0
        player_money -= 0
    return "stay"

# OpponentPlay function 
def opponentPlay():
    handR = handRank(hand)
    if handR <= 5:
        opponentPlays = raiseAmount(10)
        opponentHistory.append([opponentPlays])
        return opponentPlays
    else:
        opponentPlays = stay()
        opponentHistory.append([opponentPlays])
        return opponentPlays

# Agent Play function
def agentPlay():
    handR = handRank(hand)
    if handR <= 3:
        agentPlay = raiseAmount(10)
        opponentPlays = oppontentPlay()
        agentHistory.append([handR, agentPlay, opponentPlays])
    else:
        agentPlay = stay()
        playHistory.append([handR, agentPlay])

# Remember function
def remember():
	knowledgeBaseActions.append(actions)

# Start game function
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
	print "Opponent's hand: " + str(players[1])
	startOpponent(1)
	print "Agent's hand: " + str(players[0])
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

def unsortedSets(hand):
	amountsVals = {}
	for val in vals:
		amountsVals[val] = 0
	for card in hand:
		amountsVals[value(card)] += 1
	valueSets = []
	for item in amountsVals:
		valueSets.append(amountsVals[item])
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

# Determine the hand's second highest card
def secondHighestCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-2]

# Determine the hand's third highest card
def thirdHighestCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-3]

# Determine the hand's fourth highest card
def fourthHighestCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-4]

# Determine what player has the better straight
def bestStraight():
	# Not using this right now
	straightHolders = []
	for player in players:
		if isStraight(player):
			straightHolders.append(players.index(player))
	values1 = []
	values2 = []
	for card in players[0]:
		values1.append(value(card))
	for card in players[1]:
		values2.append(value(card))
	sortCards(values1)
	sortCards(values2)
	high1 = values1[-1]
	high2 = values2[-1]
	if high1 > high2:
		return 0
	if high2 > high1:
		return 1
	else:
		return 5

# Determine which player has the better four of a kind
def bestFourOfAKind():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	playerOnesSet = sets1.index(4)
	playerTwosSet = sets2.index(4)
	playerOnesKicker = sets1.index(1)
	playerTwosKicker = sets2.index(1)
	if playerOnesSet > playerTwosSet:
		return 0
	if playerTwosSet > playerOnesSet:
		return 1
	else:
		if playerOnesKicker > playerTwosKicker:
			return 0
		if playerTwosKicker > playerOnesKicker:
			return 1
		else:
			return 5

# Determine who has the best full house
def bestFullHouse():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	playerOnesThree = sets1.index(3)
	playerTwosThree = sets2.index(3)
	playerOnesTwo = sets1. index(2)
	playerTwosTwo = sets2.index(2)
	if playerOnesThree > playerTwosThree:
		return 0
	if playerTwosThree > playerOnesThree:
		return 1
	else:
		if playerOnesTwo > playerTwosTwo:
			return 0
		if playerTwosTwo > playerOnesTwo:
			return 1
		else:
			return 5

# Determine who has the best flush
def bestCards():
	values1 = []
	values2 = []
	for card in players[0]:
		values1.append(value(card))
	for card in players[1]:
		values2.append(value(card))
	best1 = highCard(players[0])
	best2 = highCard(players[1])
	if best1 > best2:
		return 0
	if best2 > best1:
		return 1
	else:
		nextBest1 = secondHighestCard(players[0])
		nextBest2 = secondHighestCard(players[1])
		if nextBest1 > nextBest2:
			return 0
		if nextBest2 > nextBest1:
			return 1
		else:
			thirdBest1 = thirdHighestCard(players[0])
			thirdBest2 = thirdHighestCard(players[1])
			if thirdBest1 > thirdBest2:
				return 0
			if thirdBest2 > thirdBest1:
				return 1
			else:
				fourthBest1 = fourthHighestCard(players[0])
				fourthBest2 = fourthHighestCard(players[1])
				if fourthBest1 > fourthBest2:
					return 0
				if fourthBest2 > fourthBest1:
					return 1
				else:
					low1 = lowCard(players[0])
					low2 = lowCard(players[1])
					if low1 > low2:
						return 0
					if low2 > low1:
						return 1
					else:
						return 5

# Determine who has the best three of a kind
def bestThreeOfAKind():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	playerOnesSet = sets1.index(3)
	playerTwosSet = sets2.index(3)
	playerOnesKicker = sets1.index(1)
	playerTwosKicker = sets2.index(1)
	if playerOnesSet > playerTwosSet:
		return 0
	if playerTwosSet > playerOnesSet:
		return 1
	else:
		high1 = highCard(players[0])
		high2 = highCard(players[1])
		if high1 == playerOnesSet:
			high1 = secondHighestCard(players[0])
		if high2 == playerTwosSet:
			high2 == secondHighestCard(players[1])
		if high1 > high2:
			return 0
		if high2 > high1:
			return 1
		else:
			secondHighest1 = secondHighestCard(players[0])
			secondHighest2 = secondHighestCard(players[1])
			if secondHighest1 == high1:
				secondHighest1 = thirdHighestCard(players[0])
			if secondHighest2 == high2:
				secondHighest2 = thirdHighestCard(players[1])
			if secondHighest1 > secondHighest2:
				return 0
			if secondHighest2 > secondHighest1:
				return 1
			else:
				return 5

def bestTwoPair():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	playerOnesSet = sets1.index(2)
	playerTwosSet = sets2.index(2)
	playerOnesPair = sets1.index(2,playerOnesSet + 1)
	playerTwosPair = sets2.index(2,playerTwosSet + 1)
	playerOnesSingle = sets1.index(1)
	playerTwosSingle = sets2.index(1)
	if 	((playerOnesSet > playerTwosSet) or (playerOnesSet > playerTwosPair) 
										or (playerOnesPair > playerTwosSet) 
										or (playerOnesPair > playerTwosPair)):
		return 0
	if 	((playerOnesSet < playerTwosSet) or (playerOnesSet < playerTwosPair) 
										or (playerOnesPair < playerTwosSet) 
										or (playerOnesPair < playerTwosPair)):
		return 1
	else:
		if playerOnesSingle > playerTwosSingle:
			return 0
		if playerTwosSingle > playerOnesSingle:
			return 1
		else:
			return 5


# Determine who has the best pair
def bestPair():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	playerOnesSet = sets1.index(2)
	playerTwosSet = sets2.index(2)
	if playerOnesSet > playerTwosSet:
		return 0
	if playerTwosSet > playerOnesSet:
		return 1
	else:
		high1 = highCard(players[0])
		high2 = highCard(players[1])
		if high1 == playerOnesSet:
			high1 = secondHighestCard(players[0])
		if high2 == playerTwosSet:
			high2 == secondHighestCard(players[1])
		if high1 > high2:
			return 0
		if high2 > high1:
			return 1
		else:
			secondHighest1 = secondHighestCard(players[0])
			secondHighest2 = secondHighestCard(players[1])
			if secondHighest1 == high1:
				secondHighest1 = thirdHighestCard(players[0])
			if secondHighest2 == high2:
				secondHighest2 = thirdHighestCard(players[1])
			if secondHighest1 > secondHighest2:
				return 0
			if secondHighest2 > secondHighest1:
				return 1
			else:
				thirdHighest1 = thirdHighestCard(players[0])
				thirdHighest2 = thirdHighestCard(players[1])
				if thirdHighest1 == high1:
					thirdHighest1 = fourthHighestCard(players[0])
				if thirdHighest2 == high2:
					thirdHighest2 = fourthHighestCard(players[1])
				if thirdHighest1 > thirdHighest2:
					return 0
				if thirdHighest2 > thirdHighest1:
					return 1
				else:
					return 5

# Determine who won this hand, and divvy up the pot accordingly
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
	# If more than one player has the best hand, find out whose hand is better
	# No comparison needed for Royal Flushes
	if len(playersWithBestHand) == 2:
		# Who has the better straight
		if (bestHand == 1) or (bestHand == 5):
			# Only change the list if one of them actually has a better straight
			if (bestStraight() == 0) or (bestStraight() == 1):
				playersWithBestHand = [bestStraight()]
		# Who has the better four of a kind
		if (bestHand == 2):
			if (bestFourOfAKind() == 0) or (bestFourOfAKind() == 1):
				playersWithBestHand = [bestFourOfAKind()]
		# Who has the better full house
		if (bestHand == 3):
			if (bestFullHouse() == 0) or (bestFullHouse() == 1):
				playersWithBestHand = [bestFullHouse()]
		# Who has the better flush or better high card
		if (bestHand == 4) or (bestHand == 9):
			if (bestCards() == 0) or (bestCards() == 1):
				playersWithBestHand = [bestCards()]
		# Who has the better three of a kind
		if (bestHand == 6):
			if (bestThreeOfAKind() == 0) or (bestThreeOfAKind() == 1):
				playersWithBestHand = [bestThreeOfAKind()]
		# Who has the better two pair
		if (bestHand == 7):
			if (bestTwoPair() == 0) or (bestTwoPair() == 1):
				playersWithBestHand = [bestTwoPair()]
		# Who has the better pair
		if (bestHand == 8):
			if (bestPair() == 0) or (bestPair() == 1):
				playersWithBestHand = [bestPair()]

	if bestHand == 0:
		hand = "royal flush"
	if bestHand == 1:
		hand = "straight flush"
	if bestHand == 2:
		hand = "four of a kind"
	if bestHand == 3:
		hand = "full house"
	if bestHand == 4:
		hand = "flush"
	if bestHand == 5:
		hand = "straight"
	if bestHand == 6:
		hand = "three of a kind"
	if bestHand == 7:
		hand = "two pair"
	if bestHand == 8:
		hand = "one pair"
	if bestHand == 9:
		hand = "high card"
	# Split the pot amongst the players with the best hand
	payOut = pot/len(playersWithBestHand)
	for player in playersWithBestHand:
		players_money[player] += payOut
		if len(playersWithBestHand) == 1:
			print "Player " + str(playersWithBestHand[0]) + " has won the hand with a " + hand
		else:
			winners = ""
			for player in playersWithBestHand:
				winners += player + " and "
			print "Players " + winners + " each have a " + hand + " and have split the pot evenly"

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
