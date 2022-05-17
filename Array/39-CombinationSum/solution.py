from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output_list = []
        self.cand = candidates
        self.cand_length = len(candidates)
        self.find_all_combination(0, target, [])

        return self.output_list

    def find_all_combination(self, index: int, target: int, path: List[int]):
        if target < 0:
            return
        elif target == 0:
            self.output_list.append(path)
        else:
            for i in range(index, self.cand_length):
                self.find_all_combination(i, target-self.cand[i], path+[self.cand[i]])
        return
