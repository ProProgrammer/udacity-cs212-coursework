# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????.

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


# --------------
# User Instructions
#
# Modify the function compile_formula so that the function
# it returns, f, does not allow numbers where the first digit
# is zero. So if the formula contained YOU, f would return
# False anytime that Y was 0


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y equal to 0, the function should return False."""

    # modify the code in this function.

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))

    start_letters = []
    for item in tokens:
        if item.startswith('(') and item.endswith(')'):
            start_letters.append(item.split('*')[-1][0])
    start_letter_strings_compared_with_zero = ['{} != 0'.format(x) for x in start_letters]
    single_string_of_start_letters_strings_compared_with_zero = 'and '.join(start_letter_strings_compared_with_zero)
    body = '{} and {}'.format(''.join(tokens), single_string_of_start_letters_strings_compared_with_zero)

    f = 'lambda {}: {}'.format(parms, body)
    if verbose: print f
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10 ** i, d))
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""

    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def test():
    assert not faster_solve('A + B == BA')  # should NOT return '1 + 0 == 01'
    assert faster_solve('YOU == ME**2') == ('289 == 17**2' or '576 == 24**2' or '841 == 29**2')
    assert faster_solve('X / X == X') == '1 / 1 == 1'
    return 'tests pass'

print test()
