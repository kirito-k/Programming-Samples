"""
    File name: simplify_path.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Simplify the complex path given into something linux terminal friendly command
    LeetCode: #71
    TimeComplexity: O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:

        arr = [x for x in path.split('/') if x != '' and x != '.']
        answer = []
        for elem in arr:
            if elem == '..' and answer: answer.pop()
            if elem != '..': answer.append(elem)
        a = '/' + '/'.join(answer)
        return a


def main():
    # Testcases
    s = '/a/./c////.././/../..'
    s = ''
    s = '.././/../..'
    s = 'a/b/c/d'

    sl = Solution()
    print(sl.simplifyPath(s))


if __name__ == '__main__':
    main()
