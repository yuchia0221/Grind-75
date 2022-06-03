class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = {}
        for token in s:
            try:
                memo[token] += 1
            except KeyError:
                memo[token] = 1
        
        for token in t:
            try:
                memo[token] -= 1
            except KeyError:
                return False

        return all(count == 0 for count in memo.values())