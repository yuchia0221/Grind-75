# Ransom Note

Problem can be found in [here](https://leetcode.com/problems/ransom-note)!

### [Solution](/Hash%20Table/383-RansomNote/solution.py): Hash Table

```python
def canConstruct(ransomNote: str, magazine: str) -> bool:
    memo = defaultdict(int)
    for char in magazine:
        memo[char] += 1

    for char in ransomNote:
        if memo[char] == 0:
            return False

        memo[char] -= 1

    return True
```

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n is the length of ransomNote and m is the length of magazine.
