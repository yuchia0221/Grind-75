import collections
from typing import List, Union


class TimeMap:
    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        matches = self.map[key]
        if len(matches) == 0:
            return ""
        else:
            return self.binary_seacrch(matches, timestamp)

    def binary_seacrch(self, data: List[Union[str, int]], timestamp: int) -> str:
        left, right = 0, len(data)-1

        answer = ""
        while left <= right:
            mid = left + (right-left) // 2
            if data[mid][1] <= timestamp:
                left = mid + 1
                answer = data[mid][0]
            else:
                right = mid - 1

        return answer
