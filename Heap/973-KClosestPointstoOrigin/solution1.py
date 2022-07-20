import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-self.euclidean_distance(points[i]), points[i]) for i in range(k)]
        heapq.heapify(heap)

        for i in range(k, len(points)):
            distance = -self.euclidean_distance(points[i])
            if distance > heap[0][0]:
                heapq.heappushpop(heap, (distance, points[i]))

        return [point for _, point in heap]

    def euclidean_distance(self, point: List[int]):
        return pow(point[0], 2) + pow(point[1], 2)
