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


def get_all_substrings(text):
    # start_length = len(text)
    # all_substrings = []
    #
    # # Get all substrings from a string in a list called all_substrings
    # for x in xrange(start_length):
    #     # This length will be calculated in each iteration of for loop as we will reduce the "text" by one character
    #     # in each iteration to get all the substrings from the input text
    #     length = len(text)
    #
    #     for i in xrange(length):
    #         sub_str = text[0:i + 1]
    #         all_substrings.append(sub_str)
    #
    #     text = text[1:]
    #
    # return list(set(all_substrings))

    length = len(text)
    output_list = [text[i:j+1] for i in range(length) for j in range(i, length)]
    return set(output_list)


def _list_of_substrings_with_their_lengths_sorted(all_substrings):
    return sorted(zip(all_substrings, map(len, all_substrings)), key=lambda inp: inp[1], reverse=True)


def _get_start_end_pos_of_first_palindrome_in_list_of_mapping_of_substring_with_its_length(input_list, full_text):
    """

    Args:
        input_list: list of tuples containing substrings and its length
        full_text: The full text in which we need to find the start and end position of the substring if its a
        palindrome

    Returns: start position of palindrome (pos_of_palindrome), end position of palindrome + 1 (length +
    pos_of_palindrome)

    """
    for string, length in input_list:
        if string == string[::-1]:
            pos_of_palindrome = full_text.find(string)
            return pos_of_palindrome, length + pos_of_palindrome


def longest_subpalindrome_slice(text):
    """
    Args:
        text: string in which subpalindrome has to be found

    Returns: (i, j) such that text[i:j] is the longest palindrome in text.

    """

    """
    Approach taken:
    # Get all substrings from a string
    # Create a list of tuples of all substrings with their respective lengths
    # Sort the list using length as key in reverse order (longest substring first)
    # Iterate over all substrings & check if it is a palindrome
    ## Return the position of substring in input text along with "its length + position in input text"
    """

    # Since we are case agnostic
    text = text.lower()

    # Base cases where text is an empty string or text itself is a palindrome
    if text == text[::-1]:
        return 0, len(text)

    # Backup input text into a second variable original_text as we are going to manipulate text variable inside a for
    #  loop below
    original_text = text

    all_substrings = get_all_substrings(text)

    # Create a list of tuples of all substrings with their respective lengths sorted using length as key in reverse
    # order (longest substring first)
    substrings_sorted_by_length = _list_of_substrings_with_their_lengths_sorted(all_substrings)

    # Return the position of substring in input text along with "its length + position in input text"
    return _get_start_end_pos_of_first_palindrome_in_list_of_mapping_of_substring_with_its_length(
        substrings_sorted_by_length, original_text)


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
    setup_string = """from __main__ import _list_of_substrings_with_their_lengths_sorted, get_all_substrings, _get_start_end_pos_of_first_palindrome_in_list_of_mapping_of_substring_with_its_length; all_substrings=get_all_substrings('something rac e car going'); substrings_sorted_by_length = _list_of_substrings_with_their_lengths_sorted(all_substrings);"""

    print timeit.timeit("test()", setup="from __main__ import test", number=10000)
    print timeit.timeit("longest_subpalindrome_slice('something rac e car going')",
                        setup="from __main__ import longest_subpalindrome_slice", number=10000)
    print timeit.timeit("get_all_substrings('something rac e car going')",
                        setup="from __main__ import get_all_substrings", number=10000)
    print timeit.timeit("_list_of_substrings_with_their_lengths_sorted(all_substrings)",
                        setup="from __main__ import _list_of_substrings_with_their_lengths_sorted, "
                              "get_all_substrings; all_substrings=get_all_substrings('something rac e car going')",
                        number=10000)
    print timeit.timeit("_get_start_end_pos_of_first_palindrome_in_list_of_mapping_of_substring_with_its_length("
                        "substrings_sorted_by_length, 'something rac e car going')", setup=setup_string, number=10000)


