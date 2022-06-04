class Solution:
    def longestPalindrome(self, s: str) -> int:
        memo = {}
        for token in s:
            try:
                memo[token] += 1
            except KeyError:
                memo[token] = 1

        longest_length = 0
        odd_flag = False
        for i in memo.values():
            if i % 2 == 0:
                longest_length += i
            else:
                odd_flag = True
                longest_length += (i-1)

        return longest_length + 1 if odd_flag else longest_length
