## Longest Substring Without Repeating Characters

Problem can be found in [here](https://leetcode.com/problems/longest-substring-without-repeating-characters)!

### [Solution1](/String/3-LongestSubstringWithoutRepeatingCharacters/solution1.py): Hash Table

```python
def lengthOfLongestSubstring(s: str) -> int:
    memo = {}
    max_length = pointer = 0

    for index, token in enumerate(s):
        # pointer <= memo[token] checks whether we have skipped that token before
        if token in memo and pointer <= memo[token]:
            pointer = memo[token] + 1
        else:
            max_length = max(max_length, index-pointer+1)
        memo[token] = index

    return max_length
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(m)](<https://latex.codecogs.com/svg.image?\inline&space;O(m)>), where n is the length of s and m is the length of the longest substring.

### [Solution2](/String/3-LongestSubstringWithoutRepeatingCharacters/solution2.py): Sliding Window

```python
def lengthOfLongestSubstring(s: str) -> int:
    memo = set()
    window_start = window_end = max_length = 0

    while window_start < len(s) and window_end < len(s):
        token = s[window_end]
        if token in memo:
            memo.remove(s[window_start])
            window_start += 1
        else:
            window_end += 1
            max_length = max(max_length, window_end-window_start)
            memo.add(token)

    return max_length
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(m)](<https://latex.codecogs.com/svg.image?\inline&space;O(m)>), where n is the length of s and m is the length of the longest substring.
