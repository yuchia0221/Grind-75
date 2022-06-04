# Longest Palindrome

Problem can be found in [here](https://leetcode.com/problems/longest-palindrome)!

### [Solution1](/String/409-LongestPalindrome/solution1.py): Hash Table

```python
def longestPalindrome(s: str) -> int:
    memo = {}
    for token in s:
        try:
            memo[token] += 1
        except KeyError:
            memo[token] = 1

    longest_length = 0
    odd_flag = False
    for i in memo.values():
        if i % 2 == 0:
            longest_length += i
        else:
            odd_flag = True
            longest_length += (i-1)

    return longest_length + 1 if odd_flag else longest_length
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

### [Solution2](/String/409-LongestPalindrome/solution2.py): Set

```python
def longestPalindrome(s: str) -> int:
    memo = set()
    for token in s:
        try:
            memo.remove(token)
        except KeyError:
            memo.add(token)

    has_odd_number = len(memo) > 0
    return len(s) - len(memo) + 1 if has_odd_number else len(s)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
