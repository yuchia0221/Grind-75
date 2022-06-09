from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        memo, output_list = {}, []

        for token in p:
            try:
                memo[token] += 1
            except KeyError:
                memo[token] = 1

        for right, token in enumerate(s):
            try:
                memo[token] -= 1
            except KeyError:
                memo[token] = -1

            while memo[token] < 0:
                memo[s[left]] += 1
                left += 1

            if (right-left+1) == len(p):
                output_list.append(left)

        return output_list
