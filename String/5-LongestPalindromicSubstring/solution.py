class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]
        memo = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            memo[i][i] = True

        for i in range(len(s)):
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    if i == j+1 or memo[i-1][j+1]:
                        memo[i][j] = True
                        if i-j+1 > len(longest_palindrome):
                            longest_palindrome = s[j:i+1]

        return longest_palindrome
