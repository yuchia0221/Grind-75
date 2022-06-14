# Merge Intervals

Problem can be found in [here](https://leetcode.com/problems/merge-intervals/)!

### [Solution](/Array/56-MergeIntervals/solution.py): Sorting

```python
def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sorting intervals can make sure that i.start <= i+1.start
    intervals.sort()
    output_list = [intervals[0]]

    for i in range(1, len(intervals)):
        # No Overlapping Case
        if output_list[-1][1] < intervals[i][0]:
            output_list.append(intervals[i])
        # Overlapping Case
        else:
            output_list[-1][1] = max(output_list[-1][1], intervals[i][1])

    return output_list
```

Explanation: Sorting intervals can make sure that for any 0 <= i <= size of intervals-1, intervals\[i][0]<=intervals\[i+1][0], which is a great property that we only need to change end time in overlapping cases.

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
