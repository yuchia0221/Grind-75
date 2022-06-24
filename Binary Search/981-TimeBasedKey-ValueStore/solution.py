import collections
from typing import List, Union


class TimeMap:
    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        matches = self.map[key]

        answer = ""
        left, right = 0, len(matches)-1
        while left <= right:
            mid = left + (right-left) // 2
            if matches[mid][1] <= timestamp:
                left = mid + 1
                answer = matches[mid][0]
            else:
                right = mid - 1

        return answer
