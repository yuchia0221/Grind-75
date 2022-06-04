class Solution:
    def longestPalindrome(self, s: str) -> int:
        memo = set()
        for token in s:
            try:
                memo.remove(token)
            except KeyError:
                memo.add(token)

        has_odd_number = len(memo) > 0
        return len(s) - len(memo) + 1 if has_odd_number else len(s)
