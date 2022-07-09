from typing import List


def memoization(func):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def find_next_available_job(index: int, end_time: int) -> int:
            left, right = index, len(jobs)
            while left < right:
                mid = left + (right-left) // 2
                if jobs[mid][0] >= end_time:
                    right = mid
                else:
                    left = mid + 1

            return left

        @memoization
        def find_optimal_schedule(index: int) -> int:
            if index == len(jobs):
                return 0
            next_available_job = find_next_available_job(index, jobs[index][1])
            max_profit = max(jobs[index][2]+find_optimal_schedule(next_available_job), find_optimal_schedule(index+1))
            return max_profit

        jobs = sorted(zip(startTime, endTime, profit))
        return find_optimal_schedule(0)
