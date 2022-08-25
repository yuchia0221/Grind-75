# K Closest Points to Origin

Problem can be found in [here](https://leetcode.com/problems/k-closest-points-to-origin)!

### [Solution1](/Heap/973-KClosestPointstoOrigin/solution1.py): Heap

```python
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = [(-euclidean_distance(points[i]), points[i]) for i in range(k)]
    heapq.heapify(heap)

    for i in range(k, len(points)):
        distance = -self.euclidean_distance(points[i])
        if distance > heap[0][0]:
            heapq.heappushpop(heap, (distance, points[i]))

    return [point for _, point in heap]

def euclidean_distance(point: List[int]):
    return pow(point[0], 2) + pow(point[1], 2)
```

Explanation: Since the problem is asking us to return k closest points to the origin, we can construct a heap with the first k points in the array points. After that we can iterate the remaining array, if we find the distance is larger than smallest value in the heap (notice that there is a negative sign, so smaller value indicates farther distance from the point to the origin), we can pop that value out and push the point in.

Time Complexity: ![nlogk](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogk)>), Space Complexity: ![O(k)](<https://latex.codecogs.com/svg.image?\inline&space;O(k)>), where n is the length of array and k is the number of closest points to the origin we need to return.

### [Solution2](/Heap/973-KClosestPointstoOrigin/solution2.py): Binary Search

```python
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

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of array.
