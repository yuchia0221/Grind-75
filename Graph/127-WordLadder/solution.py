from collections import deque
from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        memo = set(wordList)
        queue = deque([(beginWord, 0)])

        while queue:
            word, counter = queue.popleft()
            if word == endWord:
                return counter+1
            for i in range(len(word)):
                for char in ascii_lowercase:
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in memo:
                        memo.remove(new_word)
                        queue.append((new_word, counter+1))

        return 0
