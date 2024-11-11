#Poker Hand Simulation written by Lokesh Vaddi
import random

def countSuits():
  global flush_suit

  for card in hand:
    suit_counter[card[2]] = suit_counter.get(card[2], 0) + 1
    # Store the suit of a flush if it exists
    if suit_counter[card[2]] == 5:
      flush_suit = card[2]

def countRanks():
  for card in hand:
    rank_counter[card[0]] = rank_counter.get(card[0], 0) + 1
  
def checkRoyalFlush():
  if not flush_suit:
    return False
  
  royal_ranks = ['T','J','Q','K','A']

  for card in hand:
    if card[2] == flush_suit and card[0] in royal_ranks:
      royal_ranks.remove(card[0])
      
  if len(royal_ranks) == 0:
    return True
  
  return False

def checkStraightFlush():
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

def checkFourOfAKind():
  return 4 in list(rank_counter.values())
  
def checkFullHouse():
  num_ranks = list(rank_counter.values())
  return (2 in num_ranks and 3 in num_ranks) or num_ranks.count(3) == 2
    
def checkFlush():
  if not flush_suit:
    return False
  
  return True

def checkStraight():
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
 
def checkThreeOfAKind():
  return 3 in list(rank_counter.values())
 
def checkTwoPair():
  return list(rank_counter.values()).count(2) >= 2 

def checkPair():
  return 2 in list(rank_counter.values())


# Global Scope
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

print('How many trials should be run?')
n = int(input())

for i in range(n):
  # hand var is the 7 available cards used to make the best combination of 5 cards
  hand = random.sample(cards, 7)
  suit_counter = {}
  rank_counter = {}
  flush_suit = ''

  # Populate suit_counter, rank_counter, flush_suit
  countSuits()
  countRanks()

  if checkRoyalFlush():
    hand_type_count['Royal Flush'] += 1
  elif checkStraightFlush():
    hand_type_count['Straight Flush'] += 1
  elif checkFourOfAKind():
    hand_type_count['Four of a Kind'] += 1
  elif checkFullHouse():
    hand_type_count['Full House'] += 1
  elif checkFlush():
    hand_type_count['Flush'] += 1
  elif checkStraight():
    hand_type_count['Straight'] += 1
  elif checkThreeOfAKind():
    hand_type_count['Three of a Kind'] += 1
  elif checkTwoPair():
    hand_type_count['Two Pair'] += 1
  elif checkPair():
    hand_type_count['Pair'] += 1
  else:
    hand_type_count['High Card'] += 1

for hand_type, count in hand_type_count.items():
  print(f'{count} out of {n} ({round(100 * count / n, 2)}%) trials resulted in a {hand_type}')
