"""
    File name: count_say.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Given a specific writing pattern as follows, determine the pattern for given integer
                1.     1
                2.     11
                3.     21
                4.     1211
                5.     111221
                Each pattern is a " freq + value " pair of the number before
                Example, n = 3
                pattern for n = 2 is 11. Thus it is two times 1. Answer = 21
"""

def countSay(n):
    """
    Find the pattern for n'th number
    :param n: Integer number
    :return: 
    """

    answer = '1'
    for i in range(1, n):
        # Reset all the variables
        last = answer[0]
        freq = 0
        temp = ''

        for elem in answer:
            if last == elem:
                # Increase the frequency
                freq += 1
            else:
                # Add previous element
                temp += str(freq) + last
                last = elem
                freq = 1

        # Add previous element
        answer = temp + str(freq) + last
    return answer


def main():
    # Test cases
    n = 1
    # n = 5
    # n = 7
    print(countSay(n))

if __name__ == '__main__':
    main()