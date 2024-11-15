import poker_functions as pf
import random

if __name__ == "__main__":
    print('How many trials should be run?')
    n = int(input())

    for i in range(n):
        # hand var is the 7 available cards used to make the best combination of 5 cards
        hand = random.sample(pf.cards, 7)
       
        rank_counter = pf.countRanks(hand)
        flush_suit = pf.findFlushSuit(hand)

        if pf.checkRoyalFlush(hand, flush_suit):
            pf.hand_type_count['Royal Flush'] += 1
        elif pf.checkStraightFlush(hand, flush_suit):
            pf.hand_type_count['Straight Flush'] += 1
        elif pf.checkFourOfAKind(rank_counter):
            pf.hand_type_count['Four of a Kind'] += 1
        elif pf.checkFullHouse(rank_counter):
            pf.hand_type_count['Full House'] += 1
        elif pf.checkFlush(flush_suit):
            pf.hand_type_count['Flush'] += 1
        elif pf.checkStraight(rank_counter):
            pf.hand_type_count['Straight'] += 1
        elif pf.checkThreeOfAKind(rank_counter):
            pf.hand_type_count['Three of a Kind'] += 1
        elif pf.checkTwoPair(rank_counter):
            pf.hand_type_count['Two Pair'] += 1
        elif pf.checkPair(rank_counter):
            pf.hand_type_count['Pair'] += 1
        else:
            pf.hand_type_count['High Card'] += 1

    for hand_type, count in pf.hand_type_count.items():
        print(f'{count} out of {n} ({round(100 * count / n, 2)}%) trials resulted in a {hand_type}')