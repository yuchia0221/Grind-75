# Implement Trie (Prefix Tree)

Problem can be found in [here](https://leetcode.com/problems/implement-trie-prefix-tree)!

### [Solution](</Trie/208-ImplementTrie(PrefixTree)/solution.py>): Hash Table

```python
class Trie:
    def __init__(self):
        self.memo = {}

    def insert(self, word: str) -> None:
        current_memo = self.memo
        for char in word:
            if char not in current_memo:
                current_memo[char] = {}

            current_memo = current_memo[char]

        current_memo["."] = None

    def search(self, word: str) -> bool:
        current_memo = self.memo
        for char in word:
            if char not in current_memo:
                return False

            current_memo = current_memo[char]

        return "." in current_memo

    def startsWith(self, prefix: str) -> bool:
        current_memo = self.memo
        for char in prefix:
            if char not in current_memo:
                return False

            current_memo = current_memo[char]

        return True
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of the word.
