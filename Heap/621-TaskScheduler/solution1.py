from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurrences = Counter(tasks).values()
        max_count = max(occurrences)
        num_most_frequent_tasks = list(occurrences).count(max_count)

        return max((max_count-1) * (n+1) + num_most_frequent_tasks, len(tasks))
