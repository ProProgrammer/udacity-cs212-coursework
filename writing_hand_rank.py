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
# -------------------------------------------------
# Instructions for CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart
# or diamond.
#
# The itertools library may be helpful. Feel free to
# define multiple functions if it helps you solve the
# problem.
#
# -----------------
# Grading Notes
#
# Multiple correct answers will be accepted in cases
# where the best hand is ambiguous (for example, if
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).
# -------------------------------------------------

import itertools


def _replace_wild_card(input_hand_str, wildcard, replacement_card):
    """

    Args:
        input_hand_str: input hand in string format
        wildcard: Wildcard to replace
        replacement_card: Card to replace wildcard with

    Returns: hand in string format with that particular wild card replaced with the particular replacement_card

    """

    if replacement_card not in input_hand_str:
        return input_hand_str.replace(wildcard, replacement_card)
    return None


def hands_without_joker(hand):
    """

    Args:
        hand: a list of cards such as ['6C', '7C', '8C', '9C', 'TC', '?R', '?B']

    Returns: This function takes in a hand and if the hand has a wild card in the format ?B or ?R, it replaces the
    wild cards with all possible values (Any S or C for ?B and any H or D for ?R) and returns the list of
    hands with replaced wild cards

    """

    hand_without_wildcard = []
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    b_wildcard_replacement_suit = ["C", "S"]
    r_wildcard_replacement_suit = ["D", "H"]

    replacement_cards_for_b_wildcard = ["".join(item) for item in itertools.product(rank, b_wildcard_replacement_suit)]
    replacement_cards_for_r_wildcard = ["".join(item) for item in itertools.product(rank, r_wildcard_replacement_suit)]

    black_wildcard = "?B"
    red_wildcard = "?R"

    hand_as_str = " ".join(hand)

    if black_wildcard in hand_as_str and red_wildcard in hand_as_str:
        for replacement_black_card in replacement_cards_for_b_wildcard:
            hand_without_black_wildcard = _replace_wild_card(hand_as_str, black_wildcard, replacement_black_card)
            if hand_without_black_wildcard:
                for replacement_red_card in replacement_cards_for_r_wildcard:
                    interim_hand_without_wildcard = _replace_wild_card(hand_without_black_wildcard, red_wildcard,
                                                                       replacement_red_card)
                    if interim_hand_without_wildcard:
                        hand_without_wildcard.append(interim_hand_without_wildcard)

    elif black_wildcard in hand_as_str:
        for replacement_black_card in replacement_cards_for_b_wildcard:
            interim_hand_without_wildcard = _replace_wild_card(hand_as_str, black_wildcard, replacement_black_card)
            if interim_hand_without_wildcard:
                hand_without_wildcard.append(interim_hand_without_wildcard)

    elif red_wildcard in hand_as_str:
        for replacement_red_card in replacement_cards_for_r_wildcard:
            interim_hand_without_wildcard = _replace_wild_card(hand_as_str, red_wildcard, replacement_red_card)
            if interim_hand_without_wildcard:
                hand_without_wildcard.append(interim_hand_without_wildcard)

    else:
        hand_without_wildcard.append(hand_as_str)

    return hand_without_wildcard


def best_hand_from_list_of_hands(list_of_hands):
    """

    Args:
        list_of_hands: List of hands, each hand is a string. Eg: "6C 7C 8C 9C TC 5C 7H"

    Returns: This function gets the 5 best cards out of list of 5 or more card hands and appends it to an output list
    It then returns the max of all the cards from that output list

    """
    five_card_best_hands = [max(itertools.combinations(hand.split(), 5), key=hand_rank) for hand in list_of_hands]

    return max(five_card_best_hands, key=hand_rank)


def best_wild_hand(hand):
    """

    Args:
        hand:

    Returns:

    """
    return best_hand_from_list_of_hands(hands_without_joker(hand))


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'


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


print test_best_wild_hand()
