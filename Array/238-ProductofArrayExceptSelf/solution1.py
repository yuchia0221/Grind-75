from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_poduct, output_list = 1, []
        for number in nums:
            output_list.append(prefix_poduct)
            prefix_poduct *= number

        suffix_poduct = 1
        for i in range(len(nums) - 1, -1, -1):
            output_list[i] *= suffix_poduct
            suffix_poduct *= nums[i]

        return output_list
