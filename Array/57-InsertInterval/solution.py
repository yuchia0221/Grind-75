from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:        
        output_list = []
        for counter, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                output_list.append(interval)
            elif interval[0] > newInterval[1]:
                output_list.append(newInterval)
                return output_list + intervals[counter:]
            else:
                new_start_time = min(interval[0], newInterval[0])
                new_end_time = max(interval[1], newInterval[1])
                newInterval = [new_start_time, new_end_time]
        output_list.append(newInterval)

        return output_list
