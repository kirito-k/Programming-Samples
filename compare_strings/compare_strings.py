"""
    File name: compare_strings.py
    Language: Python 3
    Author name: Devavrat Kalam
    Description: Given string A and B (containing M and N strings separated by ','  respectively)
                Count string of A which are smaller than strings in B and make a new string representing it
    Time Complexity: O(N*M)
"""


def find_freq(s: str) -> int:
    """
    find the frequency of alphabetically first character in the string
    :param s: input string
    :return: int frequency
    """

    if not s:
        return 0

    arr = [0]*26
    # Generating frequency array for all the characters
    for elem in s:
        arr[ord(elem) - ord('a')] += 1

    ans = 0
    index = 0
    while index < len(arr):
        # find the first non 0 number, save and return it
        if arr[index] > 0:
            ans = arr[index]
            break
        index += 1

    return ans


def compare_strings(a: str, b: str) -> str:
    """
    compare two string based on the question criteria
    :param a: string of strings separated by ','
    :param b: string of strings separated by ','
    :return: string of integers separated by ','
    """

    # Separate each string to their individual
    a = a.split(',')
    b = b.split(',')
    a_freq = []
    b_freq = []
    ans = []

    # Generate a integer array of frequencies
    for elem in a:
        a_freq.append(find_freq(elem))
    # Sort it for faster precessing in future
    a_freq.sort()

    for elem in b:
        b_freq.append(find_freq(elem))

    # # Debugging
    # print(f'a: {a}')
    # print(f'b: {b}')
    # print(f'a_freq: {a_freq}')
    # print(f'b_freq: {b_freq}')

    for i in range(len(b_freq)):
        # loop through B's array
        j = 0
        count = 0
        while j < len(a_freq) and a_freq[j] < b_freq[i]:
            # Loop through A's array
            # Check if the frequency in A array is less than the B's element
            count += 1
            j += 1

        # Append the number of strings which are less than the B's element
        ans.append(count)

    return ','.join(map(str, ans))


def main():
    # Test cases
    a = 'abcd,aabc,bd'
    b = 'aaa,aa'
    # a = 'xyzzz,khjhhh,'
    # b = ',aaaaaa'

    ans = compare_strings(a, b)
    print(f'ans: {ans}')


if __name__ == '__main__':
    main()
