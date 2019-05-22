"""
    File name: sentenseReverse
    Language: Python3
    Aurhor: Devavrat Kalam
    Description: Given a list of space seperated characters, return reversed list of words in form of characters.
"""


def reverse_words(arr):
    answer = []
    start = None

    for index in range(len(arr)-1,-1,-1):
        if arr[index] != ' ':
        # If it is a character
            if start is None:
                # If word hasent started yet
                start = index
            if index == 0:
                # If this is the last character in the list, add it to answer
                answer += arr[index:start+1]

        if arr[index] == ' ':
            # If blank is found
            if start is not None:
                # A word is already started before, add it without changing its pattern
                answer += arr[index+1:start+1]
                start = None
            # We also want blanks so add them as well
            answer += ' '

    return answer


def main():
    # # Test cases:
    arr1 = ['H','e','y',' ','y','o','u',' ','w','h','a','t',' ','y','o','u',' ','w','a','n','t']
    # arr2 = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ','p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
    # arr3 = [' ', ' ', 'a', ' ']
    # arr4 = ['a', 'b']
    # arr5 = [' ', ' ']
    # arr6 = [' ', 'a']
    # arr7 = ['b', ' ']
    # arr8 = ['d']
    
    # Print analysis:
    testcase = arr1  
    print("Before:")
    print(testcase)
    print("After:")
    print(reverse_words(testcase))

if __name__ == "__main__":
    main()