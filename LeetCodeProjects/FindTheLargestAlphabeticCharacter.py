# Given a string str, our task is to find the Largest Alphabetic Character,
# whose both uppercase and lowercase are present in the string.
# The uppercase character should be returned. If there is no such character
# then return -1 otherwise print the uppercase letter of the character.
#
# Examples:
#
# Input: str = “admeDCAB”
# Output: D
# Explanation:
# Both the uppercase and lowercase characters for letter D is present in
# the string and it is also the largest alphabetical character,
# hence our output is D.

def largestCharacter(str):
    # Array for keeping track of both uppercase
    # and lowercase english alphabets
    uppercase = [False] * 26
    lowercase = [False] * 26

    arr = list(str)
    for c in arr:
        if (c.islower()):
            lowercase[ord(c) - ord('a')] = True
        if (c.isupper()):
            uppercase[ord(c) - ord('A')] = True

    # Iterate from right side of array
    # to get the largest index character
    for i in range(25, -1, -1):

        # Check for the character if both its
        # uppercase and lowercase exist or not
        if (uppercase[i] and lowercase[i]):
            return chr(i + ord('A')) + ""
    # Return -1 if no such character whose
    # uppercase and lowercase present in
    # string str
    return "-1"
