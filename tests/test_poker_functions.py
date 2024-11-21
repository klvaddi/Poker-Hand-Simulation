import pytest
import poker_functions as pf

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['2 Clubs', '2 Hearts', 'A Diamonds', '2 Diamonds', 'A Hearts', 'A Clubs', '2 Spades'], {'2': 4, 'A': 3}),
        (['A Clubs', 'K Hearts', '3 Hearts', '6 Spades', 'Q Diamonds', 'J Spades', 'T Hearts'], {'3': 1, '6': 1, 'T': 1, 'J': 1, 'Q': 1, 'K': 1, 'A': 1}),
    ]
)
def test_count_ranks(hand, expected):
    assert pf.countRanks(hand) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Spades', '7 Diamonds', '8 Hearts'], 'H'),  
        (['2 Hearts', '3 Hearts', '4 Diamonds', '5 Hearts', '6 Hearts', '7 Diamonds', '8 Spades'], None), 
    ]
)
def test_find_flush_suit(hand, expected):
    assert pf.findFlushSuit(hand) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['T Hearts', '2 Diamonds', 'J Hearts', 'Q Hearts', 'K Hearts', 'A Hearts', '3 Spades'], True),  
        (['T Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', '9 Hearts', '2 Diamonds', '3 Spades'], False), # Missing Ace of Hearts
        (['T Hearts', 'J Hearts', 'Q Diamonds', 'K Hearts', 'A Hearts', '2 Diamonds', '3 Spades'], False), # Royal straight, not flush
    ]
)
def test_check_royal_flush(hand, expected):
    flush_suit = pf.findFlushSuit(hand)
    assert pf.checkRoyalFlush(hand, flush_suit) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['T Hearts', '2 Diamonds', 'J Hearts', 'Q Hearts', 'K Hearts', '9 Hearts', '3 Spades'], True),
        (['T Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', '9 Spades', '2 Hearts', '3 Spades'], False), # Contains flush and straight but no straight flush
    ]
)
def test_check_straight_flush(hand, expected):
    flush_suit = pf.findFlushSuit(hand)
    assert pf.checkStraightFlush(hand, flush_suit) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['T Hearts', '2 Diamonds', 'T Spades', 'Q Hearts', 'T Clubs', 'T Diamonds', '3 Spades'], True),  
        (['T Hearts', 'K Spades', 'K Clubs', 'K Hearts', '9 Hearts', '9 Diamonds', '9 Spades'], False), # Has max of 3 of the same rank
    ]
)
def test_check_four_of_a_kind(hand, expected):
    rank_counter = pf.countRanks(hand)
    assert pf.checkFourOfAKind(rank_counter) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['T Hearts', 'K Spades', 'K Clubs', 'K Hearts', '9 Hearts', '9 Diamonds', '9 Spades'], True), # 3 of one rank and 3 of another
        (['T Hearts', 'K Spades', 'K Clubs', 'A Hearts', '9 Hearts', '9 Diamonds', '9 Spades'], True), # 3 of one rank and 2 of another
        (['T Hearts', 'J Hearts', 'Q Diamonds', 'K Hearts', 'A Hearts', '2 Diamonds', '3 Spades'], False),  
    ]
)
def test_check_full_house(hand, expected):
    rank_counter = pf.countRanks(hand)
    assert pf.checkFullHouse(rank_counter) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['T Diamonds', '2 Diamonds', 'J Diamonds', 'Q Hearts', 'K Diamonds', '3 Hearts', '3 Diamonds'], True), 
        (['T Diamonds', '2 Diamonds', 'J Diamonds', 'Q Hearts', 'K Diamonds', '3 Hearts', '3 Spades'], False), # Has max of 4 of one suit
    ]
)
def test_check_flush(hand, expected):
    flush_suit = pf.findFlushSuit(hand)
    assert pf.checkFlush(flush_suit) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['5 Hearts', '2 Diamonds', 'J Hearts', '4 Hearts', 'K Hearts', 'A Clubs', '3 Spades'], True), # Ace low
        (['T Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', '8 Hearts', '2 Diamonds', 'A Spades'], True), # Ace high
        (['9 Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', '8 Hearts', '2 Diamonds', 'A Spades'], False), # Has max of 3 consecutive
    
    ]
)
def test_check_straight(hand, expected):
    rank_counter = pf.countRanks(hand)
    assert pf.checkStraight(rank_counter) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['4 Hearts', '4 Diamonds', 'J Hearts', 'Q Hearts', 'K Hearts', 'A Hearts', '4 Spades'], True), 
        (['T Hearts', '4 Hearts', 'Q Hearts', 'K Hearts', '9 Hearts', '2 Diamonds', '2 Spades'], False), # Has max of 2 of the same rank
    ]
)
def test_check_three_of_a_kind(hand, expected):
    rank_counter = pf.countRanks(hand)
    assert pf.checkThreeOfAKind(rank_counter) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['T Hearts', '2 Diamonds', '2 Hearts', 'Q Hearts', 'K Diamonds', '3 Hearts', '3 Spades'], True), 
        (['T Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', '9 Hearts', '9 Diamonds', '3 Spades'], False), # Only one pair
    ]
)
def test_check_two_pair(hand, expected):
    rank_counter = pf.countRanks(hand)
    assert pf.checkTwoPair(rank_counter) == expected

@pytest.mark.parametrize(
    "hand, expected",
    [
        (['T Hearts', 'A Diamonds', 'J Hearts', 'Q Hearts', '4 Spades', 'A Hearts', '3 Spades'], True),  
        (['6 Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', '9 Hearts', '2 Diamonds', '3 Spades'], False), # No duplicate rank
    ]
)
def test_check_pair(hand, expected):
    rank_counter = pf.countRanks(hand)
    assert pf.checkPair(rank_counter) == expected

