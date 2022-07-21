from collections import Counter
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        heap = []
        occurrences = Counter(tasks).values()
        for count in occurrences:
            heapq.heappush(heap, -count)

        time, tempt = 0, []
        while heap:
            for _ in range(n+1):
                if heap or tempt:
                    time += 1
                if heap:
                    count = heapq.heappop(heap)
                    if count < -1:
                        tempt.append(count+1)

            while tempt:
                heapq.heappush(heap, tempt.pop())

        return time
