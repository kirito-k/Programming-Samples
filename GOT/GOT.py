"""
    File name: GOT1
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Find if anagram of a string can be palindrome
    Time Complexity: O( n )
"""


def gameOfThrones(s):
    """
    Determine if any anagrams of s can be a palindrome
    :param s: string
    :return:
    """

    if len(s) <= 1:
        return 'YES'

    # Creating a list for storing frequency of characters from s
    char_freq = [0]*26

    # Converting all the characters in uppercase
    s = s.upper()
    # Char counting logic
    for elem in s:
        index = ord(elem)-ord('A')
        char_freq[index] += 1

    # Counting number of characters with odd number of frequency
    odd_count = 0
    for freq in char_freq:
        if freq % 2 != 0:
            odd_count += 1

    if len(s) % 2 == 0:
        # For even
        if odd_count > 0:
            return 'NO'
    else:
        # For odd
        if odd_count > 1:
            return 'NO'

    return 'YES'



def main():
    # Test cases:
    strings = 'ss'
    # strings = 'sas'
    # strings = 'no'
    # strings = ''
    # strings = 'none'
    print(gameOfThrones(strings))


if __name__ == '__main__':
    main()
