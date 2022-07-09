# Maximum Profit in Job Scheduling

Problem can be found in [here](https://leetcode.com/problems/maximum-profit-in-job-scheduling)!

### [Solution](/Binary%20Search/1235-MaximumProfitinJobScheduling/solution.py): Dynamic Programming

```python
# Support Memorization for Dynamic Programming
def memorization(func):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def find_next_available_job(index: int, end_time: int) -> int:
            # Perform the binary search to find the smallest next available job i for the current job j
            # such that j.endtime <= i.starttime. If none, return the number of jobs.

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

            # Defined the maximum profit for interval 1 to j as OPT(j) => OPT(j) = max{j.profit + OPT(p(j)), OPT(j-1)}
            # where p(j) is the next available job for job j
            max_profit = max(jobs[index][2]+find_optimal_schedule(next_available_job), find_optimal_schedule(index+1))
            return max_profit

        jobs = sorted(zip(startTime, endTime, profit))
        return find_optimal_schedule(0)
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
