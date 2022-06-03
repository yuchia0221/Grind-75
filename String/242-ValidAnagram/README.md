# Valid Anagram

Problem can be found in [here](https://leetcode.com/problems/valid-anagram)!

### [Solution](/String/242-ValidAnagram/solution.py): Hash Table

```python
def isAnagram(s: str, t: str) -> bool:
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
