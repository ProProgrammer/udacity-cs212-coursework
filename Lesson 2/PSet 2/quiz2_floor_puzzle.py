# ------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools

# Concept Inventory:
"""
Floors:
- Top - 5th
- 4th
- 3rd
- 2nd
- Bottom - 1st

People:
- Hopper
- Liskov
- Kay
- Perlis
- Ritchie

Assignment/Relations/Constraints:
- not on top floor
- not on bottom floor
- AND combinatoin of first two (not on top floor and not on bottom floor)
- higher floor than
- floor adjacent to

Given Constraints:
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 

# Approach: There can be max of 5! repetitions if we take a brute force approach - which is 120. So lets do Brute 
Force instead of deduction
# Use itertools.permutations to get all possible arrangements of floor numbers - itertools.permutations(range(1,6))
# Assign People to each combination and check if constraints are satisfied.

"""


def floor_puzzle():
    # Your code here
    for Hopper, Kay, Liskov, Perlis, Ritchie in itertools.permutations(range(1, 6)):
        if Hopper != 5 and Kay != 1 and Liskov not in (1, 5) and Perlis > Kay and abs(Liskov - Ritchie) != 1 and abs(
                        Liskov - Kay) != 1:
            return [Hopper, Kay, Liskov, Perlis, Ritchie]


print floor_puzzle()
