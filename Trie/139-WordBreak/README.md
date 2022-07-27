# Word Break

Problem can be found in [here](https://leetcode.com/problems/word-break)!

### [Solution](/Trie/139-WordBreak/solution.py): Dynamic Programming

```python
def wordBreak(s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    has_combination = [True] + [False] * len(s)
    max_word_length = max(len(word) for word in words)
    for i in range(1, len(s)+1):
        for j in range(max(0, i-max_word_length), i):
            if not has_combination[i]:
                has_combination[i] = has_combination[j] and s[j:i] in words

    return has_combination[-1]
```

Time Complexity: ![O(n^3)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^3)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of $s$.
