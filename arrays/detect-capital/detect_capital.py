
# Point of this problem is to ensure proper capitalization
# in a string.
#
# For instance, "USA", "Google", "pumpkin" all follow poper
# capitalization rules. 
#
# However, "FlaG" does not
#
#
# Find the best solution to this problem.


# How many more cases like "USA" are there? Is it just for three
# letter acronyms?
#
# It doesn't have to be just three letters, it just has to be all
# uppercase, all lowercase, or title case

class Solution:
    def detectCapitalUse(self, word: str):
        if (word.isupper()) or (word.islower()) or (word.istitle()):
            return True
        return False


