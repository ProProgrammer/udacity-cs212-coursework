# -----------
# User Instructions
# 
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.
# # # # # Poker Rules # # # # # #
# 0 Nothing - High Card
# 1 Pair
# 2 Two Pair
# 3 Three of a Kind
# 4 Straight
# 5 Flush
# 6 Full House
# 7 Four of a Kind
# 8 Straight Flush

import itertools


def poker(hands):
    """

    Args:
        hands: List of hands such as "6C 7C 8C 9C TC 5C JS".split()

    Returns: The best hand: poker([hand,...]) => hand

    """
    return max(hands, key=hand_rank)


def hand_rank(hand):
    """

    Args:
        hand: Eg: "6C 7C 8C 9C TC 5C JS".split()

    Returns: A value indicating the ranking of a hand.

    """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush (8,11) "Jack High, Straight Flush"
        return 8, max(ranks)
    elif kind(4, ranks):  # 4 of a kind (7, 14, 12) "Four aces, Queen Kicker"
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):  # full house (6, 8, 13) "Full House, 8s over Kings"
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):  # flush (5, [10, 8, 7, 5, 3]) "Flush, 10-8"
        return 5, ranks
    elif straight(ranks):  # straight (4, 11) "Straight, Jack high"
        return 4, max(ranks)
    elif kind(3, ranks):  # 3 of a kind (3, 7, [7, 7, 7, 5, 2]) "Three 7s"
        return 3, kind(3, ranks), ranks
    elif two_pair(ranks):  # 2 pair (2, 11, 3, [13, 11, 11, 3, 3]) "2 pairs Jacks and 3s"
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):  # kind (1, 2, [13, 6, 3, 2, 2]) "Pairs of 2s, Jack high"
        return 1, kind(2, ranks), ranks
    else:  # high card (0,7,5,4,3,2) "Nothing"
        return 0, ranks


def test():
    """

    Test cases for the functions in poker program
    Returns: 'tests pass' if all assertions work, else AssertionError

    """
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99 * [fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'


# CS 212, hw1-1: 7-card stud
#
# -----------------
# User Instructions
#
# Write a function best_hand(hand) that takes a seven
# card hand as input and returns the best possible 5
# card hand. The itertools library has some functions
# that may help you solve this problem.
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).


def best_hand(hand):
    """

    Args:
        hand: A hand with at least 5 cards Eg: "6C 7C 8C 9C TC 5C JS".split()

    Returns: From a 7-card hand, return the best 5 card hand.

    """
    return max(itertools.combinations(hand, 5), key=hand_rank)


def card_ranks(hand):
    """

    Args:
        hand: Eg: "6C 7C 8C 9C TC 5C JS".split()

    Returns: A list of the ranks, sorted with higher first.

    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def flush(hand):
    """

    Args:
        hand: Eg: "6C 7C 8C 9C TC 5C JS".split()

    Returns: True if all the cards have the same suit else False

    """
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def straight(ranks):
    """

    Args:
        ranks:

    Returns: True if the ordered ranks form a 5-card straight.

    """
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def kind(n, ranks):
    """

    Args:
        n:
        ranks:

    Returns: The first rank that this hand has exactly n-of-a-kind of. Return None if there is no n-of-a-kind in the
    hand.

    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """

    Args:
        ranks:

    Returns: If there are two pair here, return the two ranks of the two pairs, else None.

    """
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return pair, low_pair
    else:
        return None


def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'


print test_best_hand()

# ##### Side work #####
# best_hand = max(list(best_hand("JD TC TH 7C 7D 7S 7H".split())), key=hand_rank)
# best_hand = max(best_hand("JD TC TH 7C 7D 7S 7H".split()), key=hand_rank)
# print best_hand
# hand = "TD TC TH 7C 7D 8C 8S".split()
# print sorted(best_hand(hand))
# best_hand_sorted_by_card_rank = card_ranks(best_hand)
# print best_hand_sorted_by_card_rank
