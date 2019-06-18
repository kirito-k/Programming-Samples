"""
    File name: string_to_int.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Convert given string to integer if possible
        Rules - A string can only be converted to integer if the first word after removing white
                spaces starts with a sign (+ or -) followed by digits. We do not care about rest of the elements
                If the integer is greater than a number which can fit inside 32 bits,
                i.e.(-2^(31) to 2^(31)-1) return the edge number of this 32 bit
                if None of the above, return 0
"""

def myAtoi(str):
    """
    Convert given string to int if possible
    :param str: string
    :return:
    """

    # Removing all the white spaces and generating a list
    str = str.strip().split()

    # If empty
    if len(str) == 0:
        return 0

    """
    Logic -
        We will index through first word only.
        We will check if it has a sign in first word
        For rest of the word, check how many digits we can gather and return it accordingly
    """

    index = 0
    word = str[index]
    if word[index] == '+' or word[index] == '-':
        index += 1

    for elem in word[index:]:
        if elem.isdigit():
            index += 1
        else:
            break

    # Take only the number part
    answer = word[:index]

    # Check for edge cases like only signs pr empty
    answer = int(answer) if (answer != '-' and answer != '+' and answer) else 0

    # Check for 32 bit number constraint
    if answer > 2147483647:
        answer = 2147483647
    elif answer < -2147483648:
        answer = -2147483648
    return answer


def main():
    # Test cases
    str = "41"
    # str = " +41    "
    # str = "-004   1"
    # str = " hello 12.23 qwsadf"
    # str = " -+12.23qwsadf hello"
    # str = " 1e2.23 qwsadf hello"
    print(myAtoi(str))


if __name__ == '__main__':
    main()