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
# Holds the opponents probability of producing each hand (where each index matches a hand rank)
opponentProbability = []
# Holds the agents probability of procucing each hand (where each index matches a hand rank)
agentProbability = []

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
		players_money.append(30)
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

# Initialize the agentProbability and opponentProbability lists to 0
x = 0
while x < 9:
    agentProbability.insert(x, 0)
    opponentProbability.insert(x, 0)
    x = x +1
print agentProbability
print opponentProbability

# Function for the Agents probability
def agentProb(hand):
    # search to see if the current hand is in a royal flush
    if hand in isRoyalFlush(hand):
        value0 = agentProbability[0]        # store the value of element 0
        value0 = value0 + 1                 # if the current hand is found increase the probability by 1
        del agentProbability[0]             # delete that current value
        agentProbability.insert(0, value0)  # insert at index 0 the new value
    else:
        value0 = agentProbability[0]
        value0 = value0 + 0
        del agentProbability[0]
        agentProbability.insert(0, value0)
    
    # search to see if the current hand is in a straight flush
    if hand in isStraightFlush(hand):
        value1 = agentProbability[1]
        value1 = value1 + 1
        del agentProbability[1]
        agentProbability.insert(1, value1)
    else:
        value1 = agentProbability[1]
        value1 = value1 + 0
        del agentProbability[1]
        agentProbability.insert(1, value1)
    
    # search to see if the current hand is in a set
    if hand in hasSet(4, hand):
        value2 = agentProbability[2]
        value2 = value2 + 1
        del agentProbability[2]
        agentProbability.insert(2, value2)
    else:
        value2 = agentProbability[2]
        value2 = value2 + 0
        del agentProbability[2]
        agentProbability.insert(2, value2)
    
    # search to see if the current hand is in a set
    if hand in (hasSet(3, hand) and hasSet(2, hand)):
        value3 = agentProbability[3]
        value3 = value3 + 1
        del agentProbability[3]
        agentProbability.insert(3, value3)
    else:
        value3 = agentProbability[3]
        value3 = value3 + 0
        del agentProbability[3]
        agentProbability.insert(3, value3)
    
    # search to see if the current hand is in a flush
    if hand in isFlush(hand):
        value4 = agentProbability[4]
        value4 = value4 + 1
        del agentProbability[4]
        agentProbability.insert(4, value4)
    else:
        value4 = agentProbability[4]
        value4 = value4 + 0
        del agentProbability[4]
        agentProbability.insert(4, value4)
    
    # search to see if the current hand is in a straight
    if hand in isStraight(hand):
        value5 = agentProbability[5]
        value5 = value5 + 1
        del agentProbability[5]
        agentProbability.insert(5, value5)
    else:
        value5 = agentProbability[5]
        value5 = value5 + 0
        del agentProbability[5]
        agentProbability.insert(5, value5)
    
    # search to see if the current hand is in a set
    if hand in hasSet(3,hand):
        value6 = agentProbability[6]
        value6 = value6 + 1
        del agentProbability[6]
        agentProbability.insert(6, value6)
    else:
        value6 = agentProbability[6]
        value6 = value6 + 0
        del agentProbability[6]
        agentProbability.insert(6, value6)
    
    # search to see if the current hand is in a two pair
    if hand in hasTwoPair(hand):
        value7 = agentProbability[7]
        value7 = value7 + 1
        del agentProbability[7]
        agentProbability.insert(7, value7)
    else:
        value7 = agentProbability[7]
        value7 = value7 + 0
        del agentProbability[7]
        agentProbability.insert(7, value7)
    
    # search to see if the current hand is in a set
    if hand in hasSet(2,hand):
        value8 = agentProbability[8]
        value8 = value8 + 1
        del agentProbability[8]
        agentProbability.insert(8, value8)
    else:
        value8 = agentProbability[8]
        value8 = value8 + 0
        del agentProbability[8]
        agentProbability.insert(8, value8)
    print agentProbability

# Function for the Opponents probability
# must change hand to the visible hand -- quick change
def opponentProb(hand):
    # search to see if the current hand is in a royal flush
    if hand in isRoyalFlush(hand):
        oppvalue0 = opponentProbability[0]          # store the value of element 0
        oppvalue0 = oppvalue0 + 1                   # if the current hand is found increase the probability by 1
        del opponentProbability[0]                  # delete that current value
        opponentProbability.insert(0, oppvalue0)    # insert at index 0 the new value
    else:
        oppvalue0 = opponentProbability[0]
        oppvalue0 = oppvalue0 + 0
        del opponentProbability[0]
        opponentProbability.insert(0, oppvalue0)
    
    # search to see if the current hand is in a straight flush
    if hand in isStraightFlush(hand):
        oppvalue1 = opponentProbability[1]
        oppvalue1 = oppvalue1 + 1
        del opponentProbability[1]
        opponentProbability.insert(1, oppvalue1)
    else:
        oppvalue1 = opponentProbability[1]
        oppvalue1 = oppvalue1 + 0
        del opponentProbability[1]
        opponentProbability.insert(1, oppvalue1)
    
    # search to see if the current hand is in a set
    if hand in hasSet(4, hand):
        oppvalue2 = opponentProbability[2]
        oppvalue2 = oppvalue2 + 1
        del opponentProbability[2]
        opponentProbability.insert(2, oppvalue2)
    else:
        oppvalue2 = opponentProbability[2]
        oppvalue2 = oppvalue2 + 0
        del opponentProbability[2]
        opponentProbability.insert(2, oppvalue2)
    
    # search to see if the current hand is in a set
    if hand in (hasSet(3, hand) and hasSet(2, hand)):
        oppvalue3 = opponentProbability[3]
        oppvalue3 = oppvalue3 + 1
        del opponentProbability[3]
        opponentProbability.insert(3, oppvalue3)
    else:
        oppvalue3 = opponentProbability[3]
        oppvalue3 = oppvalue3 + 0
        del opponentProbability[3]
        opponentProbability.insert(3, oppvalue3)
    
    # search to see if the current hand is in a flush
    if hand in isFlush(hand):
        oppvalue4 = opponentProbability[4]
        oppvalue4 = oppvalue4 + 1
        del opponentProbability[4]
        opponentProbability.insert(4, oppvalue4)
    else:
        oppvalue4 = opponentProbability[4]
        oppvalue4 = oppvalue4 + 0
        del opponentProbability[4]
        opponentProbability.insert(4, oppvalue4)
    
    # search to see if the current hand is in a straight
    if hand in isStraight(hand):
        oppvalue5 = opponentProbability[5]
        oppvalue5 = oppvalue5 + 1
        del opponentProbability[5]
        opponentProbability.insert(5, oppvalue5)
    else:
        oppvalue5 = opponentProbability[5]
        oppvalue5 = oppvalue5 + 0
        del opponentProbability[5]
        opponentProbability.insert(5, oppvalue5)
    
    # search to see if the current hand is in a set
    if hand in hasSet(3,hand):
        oppvalue6 = opponentProbability[6]
        oppvalue6 = oppvalue6 + 1
        del opponentProbability[6]
        opponentProbability.insert(6, oppvalue6)
    else:
        oppvalue6 = opponentProbability[6]
        oppvalue6 = oppvalue6 + 0
        del opponentProbability[6]
        opponentProbability.insert(6, oppvalue6)
    
    # search to see if the current hand is in a two pair
    if hand in hasTwoPair(hand):
        oppvalue7 = opponentProbability[7]
        oppvalue7 = oppvalue7 + 1
        del opponentProbability[7]
        opponentProbability.insert(7, oppvalue7)
    else:
        oppvalue7 = opponentProbability[7]
        oppvalue7 = oppvalue7 + 0
        del opponentProbability[7]
        opponentProbability.insert(7, oppvalue7)
    
    # search to see if the current hand is in a set
    if hand in hasSet(2,hand):
        oppvalue8 = opponentProbability[8]
        oppvalue8 = oppvalue8 + 1
        del opponentProbability[8]
        opponentProbability.insert(8, oppvalue8)
    else:
        oppvalue8 = opponentProbability[8]
        oppvalue8 = oppvalue8 + 0
        del opponentProbability[8]
        opponentProbability.insert(8, oppvalue8)
    return opponentProbability

# Player stay/fold
def stay(player_index):
	global actions
	if player_index == 0:
		playStr = "Agent "
	else:
		playStr = "Opponent "
	# If someone else raised, this player is folding
	if 'raised' in actions:
		inHand[player_index] = False
		print playStr + " has folded"
	# If no one raised, this player is staying
	else:
		actions.insert(player_index,'stayed')
		print playStr + "has stayed"

# Player raise
def raised(player_index):
	global pot
	global players_money
	global actions
	# make sure they have enough money to raise
	if players_money[player_index] >= 10:
		pot += 10
		players_money[player_index] -= 10
		actions.insert(player_index,'raised')
		playStr = ""
		if player_index == 0:
			playStr = "Agent "
		else:
			playStr = "Opponent "
        
		print playStr + "has raised"
	# if they ran out of money to raise, they stay an all other players stay
	else:
		stay(player_index)

# Comparison of the probabilities - determines what move the agent should make after the opponent(s) play
agentProbabilityList = []
opponentProbabilityList = []

def agentStrategy():
    agentProbabilityList = agentProb(hand)
    opponentProbabilityList = opponentProb(hand)
    # if the opponent has raised then we will assume the opponent has one of the better hands
    if (player_index != 0):
        if raised(player_index):
            # determine the opponents best probable handrank
            omaxProbability = max(opponentProbabilityList)
            bestOpponentHandRank = opponentProbabilityList.index(omaxProbability)
            
            # compare that hand rank to the agents best hand rank
            amaxProbability = max(agentProbabilityList)
            bestAgentHandRank = agentProbabilityList.index(amaxProbability)
            # if the opponents hand rank is better then fold or stay
            if (bestOpponentHandRank < bestAgentHandRank):
                stay(0) # make the agent stay
            else:
                raised(0)
        else:
        # make the opponent play first
        startOpponent(index)

# Remove players from list if they have run out of money
def checkPlayers():
	global players_money
	global inGame
	agentmoney = players_money[0]
	opponentmoney = players_money[1]
	if agentmoney <= 0:
		inGame[0] = False
	if opponentmoney <= 0:
		inGame[1] = False

# Start opponent(s)
def startOpponent(index):
	global actions
	playStr = ""
	if index == 0:
		playStr = "Agent"
	else:
		playStr = "Opponent"
	rank = handRank(players[index])
    # pick strategy for this entire game
    opponentStrategy = random.randrange(1,2)
    if (opponentStrategy == 1):
        # Raise if hand is a straight or better
        if rank < 6:
            raised(index)
        else:
            stay(index)
#elif (opponentStrategy == 2):
        


# Start agent
def startAgent():
	global actions
	index = 0
	rank = handRank(players[index])
    agentProb(hand)
    opponentProb(hand)      # must be changed to the visible cards
	playStr = ""
	if index == 0:
		playStr = "Agent"
	else:
		playStr = "Opponent"
	# How good is your hand?
        #if   (not 'raised' in actions) and (rank < 5):
            #raised(index)
	# Did the opponents raise?
        #elif 'raised' in actions:
		# Agent has better than a pair, raise
            #if rank < 8:
#raised(index)
        #else:
#stay(index)

# The cards after the first card are all visible to all players
def visibleCards(player):
	return	players[player][1:]

# Get the rank of the hand (a lower number is a better hand)
def handRank(hand):
	if   isRoyalFlush(hand):					return 0
	elif isStraightFlush(hand):					return 1
	elif hasSet(4,hand):						return 2
	elif (hasSet(3,hand) and hasSet(2,hand)):	return 3
	elif isFlush(hand):							return 4
	elif isStraight(hand):						return 5
	elif hasSet(3,hand):						return 6
	elif hasTwoPair(hand):						return 7
	elif hasSet(2,hand):						return 8
	else:										return 9 # They got nothing

# Remember function (don't know if we still need this)
def remember():
	knowledgeBaseActions.append(actions)

# Start game function
def startGame():
	addPlayersStart(2)
	while not gameOver():
		startHand()
	if gameOver():
		whoWonGame()

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
	# Look for specific case where the Ace is a low Ace (a "1", let's say)
	#   (instead of the usual high Ace, what would be a "14")
	if (('A' in values) and ('2' in values) and ('3' in values)
        and ('4' in values) and ('5' in values)):
		return True
	else:
		# Pick out the low card and create a list, starting from the low card's
		#   index until you reach 5
		low = vals.index(lowCard(hand))
		rangeUp = range(low,low + 5)
		ranks = []
		for val in values:
			ranks.append(vals.index(val))
		ranks.sort()
		# Compare the sorted ranks with the previously created range
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

# Find the sets of a hand and return an unsorted list with the number of
#   occurances of each card (for when I want to know which card value had what
#   number of occurances)
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
#  (if first argument is 2, will return true if the hand has a pair, etc)
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

# Determine the hand's nth highest card
def whatHighestCard(hand,what):
	negated = 0 - what
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	#  This list goes up (low to high)
	return values[negated]

# Determine the hand's high card (where Ace is the highest possible card)
def highCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-1]

# Determine the hand's second highest card (for comparisons of hands)
#  Yes, I'm not proud of the need to include something like this and this could
#  easily be made into one function that takes an additional argument, but I
#  just wanted to get this running
def secondHighestCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-2]

# Determine the hand's third highest card (for comparisons of hands)
def thirdHighestCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-3]

# Determine the hand's fourth highest card (for comparisons of hands)
def fourthHighestCard(hand):
	values = []
	for card in hand:
		values.append(value(card))
	values = sortCards(values)
	return values[-4]

# Determine what player has the better straight
#   You really only need to know that 1) they both have straights and 2) the
#   high card for each straight
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

# Determine which player has the best four of a kind
def bestFourOfAKind():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	playerOnesSet = sets1.index(4)
	playerTwosSet = sets2.index(4)
	if playerOnesSet > playerTwosSet:
		return 0
	if playerTwosSet > playerOnesSet:
		return 1
	# This is only necessary if/when there are multiple decks
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
	# This is only necessary if/when there are multiple decks
	else:
		if playerOnesTwo > playerTwosTwo:
			return 0
		if playerTwosTwo > playerOnesTwo:
			return 1
		else:
			return 5

# Determine who has the best flush (yes, this looks incredibly painful)
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
	# If they both have the same high card, start checking the next best card(s)
	else:
		if len(values1) > 1:
			nextBest1 = whatHighestCard(players[0],2)
			nextBest2 = whatHighestCard(players[1],2)
			if nextBest1 > nextBest2:
				return 0
			if nextBest2 > nextBest1:
				return 1
			else:
				if len(values1) > 2:
					thirdBest1 = whatHighestCard(players[0],3)
					thirdBest2 = whatHighestCard(players[1],3)
					if thirdBest1 > thirdBest2:
						return 0
					if thirdBest2 > thirdBest1:
						return 1
					else:
						if len(values1) > 3:
							fourthBest1 = whatHighestCard(players[0],4)
							fourthBest2 = whatHighestCard(players[1],4)
							if fourthBest1 > fourthBest2:
								return 0
							if fourthBest2 > fourthBest1:
								return 1
							else:
								if len(values1) > 4:
									low1 = lowCard(players[0])
									low2 = lowCard(players[1])
									if low1 > low2:
										return 0
									if low2 > low1:
										return 1
									else:
										return 5
								else:
									return 5
						else:
							return 5
				else:
					return 5
		else:
			return 5

# Determine who has the best three of a kind
def bestThreeOfAKind():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	countT1 = sets1.count(3)
	countT2 = sets2.count(3)
	# Necessary debug
	if countT1 > 0:
		playerOnesSet = sets1.index(3)
	else:
		return 5
	if countT2 > 0:
		playerTwosSet = sets2.index(3)
	else:
		return 5
	# Compare the sets of three for each player, see who's is better
	if playerOnesSet > playerTwosSet:
		return 0
	if playerTwosSet > playerOnesSet:
		return 1
	# This is only necessary if/when there are multiple decks
	else:
		high1 = highCard(players[0])
		high2 = highCard(players[1])
		if high1 == playerOnesSet:
			high1 = whatHighestCard(players[0],2)
		if high2 == playerTwosSet:
			high2 == whatHighestCard(players[1],2)
		if high1 > high2:
			return 0
		if high2 > high1:
			return 1
		else:
			secondHighest1 = whatHighestCard(players[0],2)
			secondHighest2 = whatHighestCard(players[1],2)
			if secondHighest1 == high1:
				secondHighest1 = whatHighestCard(players[0],3)
			if secondHighest2 == high2:
				secondHighest2 = whatHighestCard(players[1],3)
			if secondHighest1 > secondHighest2:
				return 0
			if secondHighest2 > secondHighest1:
				return 1
			else:
				return 5

def bestTwoPair():
	sets1 = unsortedSets(players[0])
	sets2 = unsortedSets(players[1])
	counts1= sets1.count(2)
	counts2 = sets2.count(2)
	single1 = sets1.count(1)
	single2 = sets2.count(1)
	# Necessary debug (as in bestPair)
	if counts1 >= 2:
		playerOnesSet = sets1.index(2)
		playerOnesPair = sets1.index(2,playerOnesSet + 1)
	else:
		return 5
	if counts2 >= 2:
		playerTwosSet = sets2.index(2)
		playerTwosPair = sets2.index(2,playerTwosSet + 1)
	else:
		return 5
	if single1 >= 1:
		playerOnesSingle = sets1.index(1)
	else:
		return 5
	if single2 >= 1:
		playerTwosSingle = sets2.index(1)
	else:
		return 5
	# If either of player ones sets bests all of player twos sets,
	#   they've the best two pair
	if 	((playerOnesSet > playerTwosSet) or (playerOnesSet > playerTwosPair)
         or (playerOnesPair > playerTwosSet)
         or (playerOnesPair > playerTwosPair)):
		return 0
	# If either of player twos sets bests all of player ones sets,
	#   they've the best two pair
	if 	((playerOnesSet < playerTwosSet) or (playerOnesSet < playerTwosPair)
         or (playerOnesPair < playerTwosSet)
         or (playerOnesPair < playerTwosPair)):
		return 1
	# Otherwise, compare their kickers (the non-pair card)
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
	# From debug, it hits bestPair even when a player doesn't have one
	if 2 in sets1:
		playerOnesSet = sets1.index(2)
	else:
		return 5
	if 2 in sets2:
		playerTwosSet = sets2.index(2)
	else:
		return 5
	# The normal bits
	if playerOnesSet > playerTwosSet:
		return 0
	if playerTwosSet > playerOnesSet:
		return 1
	else:
		high1 = highCard(players[0])
		high2 = highCard(players[1])
		if high1 == playerOnesSet:
			high1 = whatHighestCard(players[0],2)
		if high2 == playerTwosSet:
			high2 == whatHighestCard(players[1],2)
		if high1 > high2:
			return 0
		if high2 > high1:
			return 1
		else:
			secondHighest1 = whatHighestCard(players[0],2)
			secondHighest2 = whatHighestCard(players[1],2)
			if secondHighest1 == high1:
				secondHighest1 = whatHighestCard(players[0],3)
			if secondHighest2 == high2:
				secondHighest2 = whatHighestCard(players[1],3)
			if secondHighest1 > secondHighest2:
				return 0
			if secondHighest2 > secondHighest1:
				return 1
			else:
				thirdHighest1 = whatHighestCard(players[0],3)
				thirdHighest2 = whatHighestCard(players[1],3)
				if thirdHighest1 == high1:
					thirdHighest1 = whatHighestCard(players[0],4)
				if thirdHighest2 == high2:
					thirdHighest2 = whatHighestCard(players[1],4)
				if thirdHighest1 > thirdHighest2:
					return 0
				if thirdHighest2 > thirdHighest1:
					return 1
				else:
					return 5

# When only one person is left in the hand, they've won
def whoWonTheyWon(winner):
	global pot
	global players_money
	players_money[winner] += pot
	pot = 0
	playStr = ""
	if playersWithBestHand[0] == 0:
		playStr = "Agent"
	else:
		playStr = "Opponent"
	print playStr + " was the only one left in the hand." + playStr + " has won the hand"

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
	# Create a string of the best hand
	if bestHand == 0: hand = "royal flush"
	if bestHand == 1: hand = "straight flush"
	if bestHand == 2: hand = "four of a kind"
	if bestHand == 3: hand = "full house"
	if bestHand == 4: hand = "flush"
	if bestHand == 5: hand = "straight"
	if bestHand == 6: hand = "three of a kind"
	if bestHand == 7: hand = "two pair"
	if bestHand == 8: hand = "one pair"
	if bestHand == 9: hand = "high card"
	# Split the pot amongst the players with the best hand
	payOut = pot/len(playersWithBestHand)
	for player in playersWithBestHand:
		players_money[player] += payOut
		if len(playersWithBestHand) == 1:
			playStr = ""
			if playersWithBestHand[0] == 0:
				playStr = "Agent"
			else:
				playStr = "Opponent"
			print playStr + " has won the hand with a " + hand
		else:
			# Leaving this stuff in for now (aka, in case there are more
			#   opponents)
			"""
                winners = ""
                for player in playersWithBestHand:
				playStr = ""
				if player == 0:
                playStr = "Agent"
				else:
                playStr = "Opponent"
				winners += playStr
                """
			print "Agent and Opponent each have a " + hand + " and have split the pot evenly"

# Figure out is over (check how many players are left in the game)
def gameOver():
	checkPlayers()
	playersLeft = inGame.count(True)
	if playersLeft == 1:
		return True
	else:
		return False

# Determine who won the game (aka, the only person left in the game)
def whoWonGame():
	playersLeft = inGame.count(True)
	if playersLeft == 1:
		winner = inGame.index(True)
		playStr = ""
		if winner == 0:
			playStr = "Agent"
		if winner == 1:
			playStr = "Opponent"
		print playStr + " has won the game with " + str(players_money[winner]) + " credits"

# Determine who has the better of the same hand
# If the hands are equally good (best*****() returns 5), pick a player at random
def compareSameHands(rank):
	if rank == 0:
		return random.randint(0,1)
	if rank == 1:
		stra = bestStraight()
		if stra == 5:
			return random.randint(0,1)
		else:
			return stra
	if rank == 2:
		return bestFourOfAKind()
	if rank == 3:
		fh = bestFullHouse()
		if fh == 5:
			return random.randint(0,1)
		else:
			return fh
	if rank == 4:
		fl = bestCards()
		if fl == 5:
			return random.randint(0,1)
		else:
			return fl
	if rank == 5:
		strai = bestStraight()
		if strai == 5:
			return random.randint(0,1)
		else:
			return strai
	if rank == 6:
		thr = bestThreeOfAKind()
		if thr == 5:
			return random.randint(0,1)
		else:
			return thr
	if rank == 7:
		twp = bestTwoPair()
		if twp == 5:
			return random.randint(0,1)
		else:
			return twp
	if rank == 8:
		pai = bestPair()
		if pai == 5:
			return random.randint(0,1)
		else:
			return pai
	if rank == 9:
		hc = bestCards()
		if hc == 5:
			return random.randint(0,1)
		else:
			return hc

# In the first round, deal two cards to each player, the first is hidden to all other players
#  the subsequent cards are all visible to all players
#  In all other rounds, deal one card to each player (visible)
#  Start a round of betting
def bets():
	agentsVisible = visibleCards(0)
	opponentsVisible = visibleCards(1)
	# See who goes first this round, based on the person with the best visible cards
	#  On first round, person with highest card starts the round of bets
	if len(players[0]) == 1:
		highAgent = vals.index(lowCard(agentsVisible))
		highOpponent = vals.index(lowCard(opponentsVisible))
		if highAgent > highOpponent:
			print "Agent's hand: " + str(players[0])
			startAgent()
			print "Opponent's hand: " + str(players[1])
			startOpponent(1)
		else:
			print "Opponent's hand: " + str(players[1])
			startOpponent(1)
			print "Agent's hand: " + str(players[0])
			startAgent()
	else:
		agentRank = handRank(agentsVisible)
		opponentRank = handRank(opponentsVisible)
		if agentRank > opponentRank:
			print "Agent's hand: " + str(players[0])
			startAgent()
			print "Opponent's hand: " + str(players[1])
			startOpponent(1)
		if opponentRank > agentRank:
			print "Opponent's hand: " + str(players[1])
			startOpponent(1)
			print "Agent's hand: " + str(players[0])
			startAgent()
		else:
			whoGoes = compareSameHands(agentRank)
			if whoGoes == 0:
				print "Agent's hand: " + str(players[0])
				startAgent()
				print "Opponent's hand: " + str(players[1])
				startOpponent(1)
			else:
				print "Opponent's hand: " + str(players[1])
				startOpponent(1)
				print "Agent's hand: " + str(players[0])
				startAgent()

# Setup deck and deal hands to each player, start each round of betting after
#   each round of dealing, and find out who won
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
	deal(2)
	bets()
	if len(inHand) > 1:
		deal(1)
		bets()
		if len (inHand) > 1:
			deal(1)
			bets()
			if len(inHand) > 1:
				deal(1)
				bets()
				finishHand()
			else:
				finishHand()
		else:
			finishHand()
	else:
		finishHand()

# All bets are in, figure out who won this hand
def finishHand():
	if len(inHand) > 1:
		whoWon()
	else:
		whoOneTheyWon(inHand.index(True))
	remember()
	print players_money

startGame()

