from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        memo = defaultdict(int)
        for char in magazine:
            memo[char] += 1

        for char in ransomNote:
            if memo[char] == 0:
                return False

            memo[char] -= 1

        return True
