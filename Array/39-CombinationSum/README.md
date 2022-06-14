# Combination Sum

Problem can be found in [here](https://leetcode.com/problems/combination-sum)!

### [Solution](/Array/39-CombinationSum/solution.py): Backtracking

```python
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def find_all_combination(index: int, target: int, path: List[int]):
        if target < 0:
            return
        elif target == 0:
            output_list.append(path)
        else:
            for i in range(index, cand_length):
                find_all_combination(i, target-cand[i], path+[cand[i]])
        return

    output_list = []
    cand = candidates
    cand_length = len(candidates)
    find_all_combination(0, target, [])

    return output_list
```

Explanation: The algorithm is simple; just use backtracking techniques. Noted that we use variable index to avoid duplicated combination. So, whenever index becomes larger, we cannot choose number before the index element in candidates array.

Time Complexity: ![O(2^k)](<https://latex.codecogs.com/svg.image?\inline&space;O(2^k)>), where k is the number of tree nodes of the recursion tree. In this given problem, k is the sum of target/candidates[i] from i=0 to len(candidates)-1.

Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of longest combination. In worst case scenario, N = target when 1 is in the candidates array.
