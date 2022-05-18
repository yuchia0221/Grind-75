from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
