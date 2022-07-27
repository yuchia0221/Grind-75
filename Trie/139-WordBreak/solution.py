from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        has_combination = [True] + [False] * len(s)
        max_word_length = max(len(word) for word in words)
        for i in range(1, len(s)+1):
            for j in range(max(0, i-max_word_length), i):
                if not has_combination[i]:
                    has_combination[i] = has_combination[j] and s[j:i] in words

        return has_combination[-1]
