from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output_list = []
        visited_numbers = set()
        self.dfs(nums, output_list, visited_numbers, [])
        return output_list

    def dfs(self, nums: List[int], output_list: List[List[int]], visited_numbers: Set[int], tempt: List[int]) -> None:
        if len(tempt) == len(nums):
            output_list.append(tempt[:])
            return

        for number in nums:
            if number not in visited_numbers:
                visited_numbers.add(number)
                tempt.append(number)
                self.dfs(nums, output_list, visited_numbers, tempt)
                tempt.pop()
                visited_numbers.remove(number)
