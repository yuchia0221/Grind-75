# Insert Interval

Problem can be found in [here](https://leetcode.com/problems/insert-interval)!

### [Solution](/Array/57-InsertInterval/solution.py)

```python
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    output_list = []
    for counter, interval in enumerate(intervals):
        if interval[1] < newInterval[0]:                   # No intersection of two intervals
            output_list.append(interval)
        elif interval[0] > newInterval[1]:
            output_list.append(newInterval)
            return output_list + intervals[counter:]
        else:                                              # Overlap Cases
            new_start_time = min(interval[0], newInterval[0])
            new_end_time = max(interval[1], newInterval[1])
            newInterval = [new_start_time, new_end_time]
    output_list.append(newInterval)

    return output_list
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
