"""
    File name: paranthesis.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Return a string removing the outermost parenthesis from every bracket.
    LeetCode: #1021
    TimeComplexity: O(n)
"""
from collections import deque


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        dq = deque()
        open_bracks = 0
        answer = ''
        for s in S:
            if s == '(':
                if open_bracks != 0:
                    answer += s
                open_bracks += 1
                dq.append(s)
            else:
                if open_bracks != 1:
                    answer += s
                open_bracks -= 1
                dq.pop()
        return answer


def main():
    # Testcases
    arr = '()((()))()'
    # arr = '()()()'
    # arr = '()(()())((()))'
    # arr = ''

    s = Solution()
    print(s.removeOuterParentheses(arr))


if __name__ == '__main__':
    main()
