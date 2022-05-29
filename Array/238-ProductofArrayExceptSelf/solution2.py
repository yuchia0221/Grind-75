from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list = [1] * len(nums)
        prefix_poduct = suffix_poduct = 1
        for index, number in enumerate(nums):
            output_list[index] *= prefix_poduct
            prefix_poduct *= number
            output_list[-1-index] *= suffix_poduct
            suffix_poduct *= nums[-1-index]

        return output_list
