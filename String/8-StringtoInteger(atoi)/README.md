# String to Integer (atoi)

Problem can be found in [here](https://leetcode.com/problems/string-to-integer-atoi)!

### [Solution](</String/8-StringtoInteger(atoi)/solution.py>)

```python
def myAtoi(s: str) -> int:
    answer = index = sign = 0
    MAX_INT, MIN_INT = 2147483647, -2147483648

    s = s.strip()
    if len(s) == 0:
        return 0

    sign = -1 if s[0] == "-" else 1
    if s[0] in set("+-"):
        index += 1

    while index < len(s) and s[index].isdigit():
        # In ASCII, int(s[index]) = ord(s[index]) - ord("0")
        answer = answer * 10 + int(s[index])
        index += 1

    answer *= sign
    # Make sure the returned value is in [-2^31, 2^31)
    answer = min(MAX_INT, max(answer, MIN_INT))
    return answer
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
