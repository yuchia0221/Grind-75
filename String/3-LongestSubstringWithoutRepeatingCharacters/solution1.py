class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        max_length = pointer = 0

        for index, token in enumerate(s):
            if token in memo and pointer <= memo[token]:
                pointer = memo[token] + 1
            else:
                max_length = max(max_length, index-pointer+1)
            memo[token] = index

        return max_length
