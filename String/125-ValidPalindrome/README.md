# Valid Palindrome

Problem can be found in [here](https://leetcode.com/problems/valid-palindrome)!

### [Solution1](/String/125-ValidPalindrome/solution1.py): Python String Functions

```python
def isPalindrome(s: str) -> bool:
    s = "".join(char for char in s if char.isalnum()).lower()
    return s == s[::-1]
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [Solution2](/String/125-ValidPalindrome/solution2.py): Two Pointers

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s)-1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right += 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right += 1

    return True
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
