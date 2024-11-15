# Used to create cards
ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['Clubs','Hearts','Spades','Diamonds']
cards = []

# Create the 52 cards in a standard deck
for i in ranks:
  for x in suits:
    cards.append(i + ' ' + x)

# Used to check for straights
rank_dict = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 1
}

# Maintains number of occurences of each hand type
hand_type_count = {
    'Royal Flush': 0,
    'Straight Flush': 0,
    'Four of a Kind': 0,
    'Full House': 0,
    'Flush': 0,
    'Straight': 0,
    'Three of a Kind': 0,
    'Two Pair': 0,
    'Pair': 0,
    'High Card': 0
}


# Returns a dictionary containing the count of each rank in hand
def countRanks(hand):
  rank_counter = {}

  for card in hand:
    rank_counter[card[0]] = rank_counter.get(card[0], 0) + 1

  return rank_counter

# Returns the suit of a flush if it exists
def findFlushSuit(hand):
  suit_counter = {}

  for card in hand:
    suit_counter[card[2]] = suit_counter.get(card[2], 0) + 1
    if suit_counter[card[2]] == 5:
      return card[2]
    
  return None

def checkRoyalFlush(hand, flush_suit):
  if not flush_suit:
    return False
  
  royal_ranks = ['T','J','Q','K','A']

  for card in hand:
    if card[2] == flush_suit and card[0] in royal_ranks:
      royal_ranks.remove(card[0])
      
  if len(royal_ranks) == 0:
    return True
  
  return False

def checkStraightFlush(hand, flush_suit):
  if not flush_suit:
    return False

  # Find all rank values of cards in hand that match the flush suit
  rank_vals = []
  for card in hand:
    if card[2] == flush_suit:
      rank_vals.append(rank_dict[card[0]])
 
  rank_vals.sort()

  # Check for a straight among cards of the flush suit
  consecutive = 1
  for i in range(len(rank_vals) - 1):
    if rank_vals[i] + 1 == rank_vals[i+1]:
      consecutive += 1
    else:
      consecutive = 1
    if consecutive == 5:
      return True
  
  return False

def checkFourOfAKind(rank_counter):
  return 4 in rank_counter.values()
  
def checkFullHouse(rank_counter):
  num_ranks = list(rank_counter.values())
  return (2 in num_ranks and 3 in num_ranks) or num_ranks.count(3) == 2
    
def checkFlush(flush_suit):
  return bool(flush_suit)
    
def checkStraight(rank_counter):
  if len(rank_counter) < 5:
    return False
  
  rank_vals = []
  for rank in rank_counter:
    rank_vals.append(rank_dict[rank])

  # Account for Ace having a value of 1 or 14 in a straight
  if 1 in rank_vals:
    rank_vals.append(14)

  rank_vals.sort()

  consecutive = 1
  for i in range(len(rank_vals) - 1):
    if rank_vals[i] + 1 == rank_vals[i+1]:
      consecutive += 1
    else:
      consecutive = 1
    if consecutive == 5:
      return True
  
  return False
 
def checkThreeOfAKind(rank_counter):
  return 3 in rank_counter.values()
 
def checkTwoPair(rank_counter):
  return list(rank_counter.values()).count(2) >= 2 

def checkPair(rank_counter):
  return 2 in rank_counter.values()