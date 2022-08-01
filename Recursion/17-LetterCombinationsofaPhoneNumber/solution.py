from typing import List


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
