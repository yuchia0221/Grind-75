# Letter Combinations of a Phone Number

Problem can be found in [here](https://leetcode.com/problems/letter-combinations-of-a-phone-number)!

### [Solution](/Recursion/17-LetterCombinationsofaPhoneNumber/solution.py): Recursion

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digit2letter = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output_list = []
        if digits:
            self.dfs(output_list, digits, 0, [])
        return output_list

    def dfs(self, output_list: List[str], digits: str, index: int, tempt: List[int]):
        if len(digits) == index:
            output_list.append("".join(tempt))
            return

        for letter in self.digit2letter[digits[index]]:
            tempt.append(letter)
            self.dfs(output_list, digits, index+1, tempt)
            tempt.pop()
```

Time Complexity: ![O(4^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(4^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of array $digits$.
