from typing import List, Tuple


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.remaining_points = list(range(len(points)))
        self.distances = [self.squared_distance(point) for point in points]

        closest_points = []
        low, high = 0, max(self.distances)
        while k:
            mid = (low+high) / 2
            self.binary_search(mid)
            if len(self.closer) > k:
                self.remaining_points = self.closer
                high = mid
            else:
                low = mid
                k -= len(self.closer)
                self.remaining_points = self.farther
                closest_points.extend(self.closer)

        return [points[i] for i in closest_points]

    def binary_search(self, threshold: int):
        self.closer, self.farther = [], []
        for i in self.remaining_points:
            if self.distances[i] > threshold:
                self.farther.append(i)
            else:
                self.closer.append(i)

    def squared_distance(self, point: List[int]):
        return pow(point[0], 2) + pow(point[1], 2)
