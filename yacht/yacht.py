"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    result = 0
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        for x in dice:
            if x == category:
                result += category
    elif category == 7:
        for i in range(1,7):
            for j in range(1,7):
                if dice.count(i) == 3 and dice.count(j) == 2:
                    return 3*i + 2*j
    elif category == 8:
        for i in range(1,7):
            if dice.count(i) >= 4:
                return 4*i
    elif category == 9:
        if set([1,2,3,4,5]).issubset(dice):
            return 30
    elif category == 10:
        if set([2,3,4,5,6]).issubset(dice):
            return 30
    elif category == 11:
        return sum(dice)
    elif category == 50:
        for i in range(1,7):
            if dice.count(i) == 5:
                return category
    return result
