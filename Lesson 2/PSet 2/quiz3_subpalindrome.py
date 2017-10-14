# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficiency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


"""
Idea for the nested for loop to get all substrings took birth this way:

# print '2. a_string[0:i+1]'
# print 'length:', length
# for i in xrange(length):
#     print 'value of i in first loop:', i
#     sub_str = a_string[0:i+1]
#     print sub_str
#     all_substrings.append(sub_str)

# print '\n\n'
# print 'Loop 2 of 2. a_string[0:i+1]'
# a_string = a_string[1:]
# length = len(a_string)
# print 'length:', length
# for i in xrange(length):
#     print 'value of i in second loop:', i
#     sub_str = a_string[0: i+1]
#     print sub_str
#     all_substrings.append(sub_str)

# print '\n\n'
# print 'Loop 3 of 2. a_string[0:i+1]'
# a_string = a_string[1:]
# length = len(a_string)
# print 'length:', length
# for i in xrange(length):
#     print 'value of i in third loop:', i
#     sub_str = a_string[0: i+1]
#     print sub_str
#     all_substrings.append(sub_str)

"""


def get_all_substrings_sorted_by_length(text):

    length = len(text)
    return sorted([text[i:j+1] for i in range(length) for j in range(i, length)], key=len, reverse=True)


def get_palindrome_strings(list_of_substrings):
    return (x for x in list_of_substrings if x == x[::-1])


def get_start_pos_end_pos_of_a_sub_string(substring, fullstring):
    start_pos = fullstring.find(substring)
    end_pos = start_pos + len(substring)
    return start_pos, end_pos


def longest_subpalindrome_slice(text):
    """
    Args:
        text: string in which subpalindrome has to be found

    Returns: (i, j) such that text[i:j] is the longest palindrome in text.

    """

    """
    Approach taken:
    # Get all substrings from a string sorted by length
    # Yield on first palindrome from list of already sorted substrings
    # Return the start and end position of first palindrome in the sorted list
    """

    # Since we are case agnostic
    text = text.lower()

    # Base cases where text is an empty string or text itself is a palindrome
    if text == text[::-1]:
        return 0, len(text)

    all_substrings_reverse_sorted = get_all_substrings_sorted_by_length(text)
    palindrome = get_palindrome_strings(all_substrings_reverse_sorted).next()
    return get_start_pos_end_pos_of_a_sub_string(palindrome, text)


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print test()

if __name__ == '__main__':
    import timeit
    print timeit.timeit("test()", setup="from __main__ import test", number=10000)
    print timeit.timeit("longest_subpalindrome_slice('something rac e car going')",
                        setup="from __main__ import longest_subpalindrome_slice", number=10000)
    print timeit.timeit("get_all_substrings_sorted_by_length('something rac e car going')",
                        setup="from __main__ import get_all_substrings_sorted_by_length", number=10000)
    print timeit.timeit("get_palindrome_strings(all_substrings)",
                        setup="from __main__ import get_palindrome_strings, get_all_substrings_sorted_by_length; "
                              "all_substrings=get_all_substrings_sorted_by_length('something rac e car going')",
                        number=10000)
    # longest_subpalindrome_slice('something rac e car going')
