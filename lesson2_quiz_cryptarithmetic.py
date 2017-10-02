# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????.

import cProfile
import itertools
import re
import string


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    """
    Generate all possible fillings-in of letters in formula with digits.

    Args:
        formula: String representation of formula with letters

    Returns: String representation of formula with digits

    """
    list_of_words = re.findall("[a-zA-Z]+", formula)
    all_letters = [c for word in list_of_words for c in word]
    unique_letters = set(all_letters)
    letters = "".join(unique_letters)

    permutations_size = len(letters)

    for digits in itertools.permutations('1234567890', permutations_size):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


# cProfile.run("print solve('ODD + ODD == EVEN')")

# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)'
# Non-uppercase words should remain unchaged.


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('{}*{}'.format(10 ** i, d))
                 for (i, d) in enumerate(word[::-1])]
        return '({})'.format('+'.join(terms))
    else:
        return word

# cProfile.run('print compile_word("DeePLs123D")')
