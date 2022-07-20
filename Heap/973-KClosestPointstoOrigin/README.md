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

Time Complexity: ![nlogk](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogk)>), Space Complexity: ![O(k)](<https://latex.codecogs.com/svg.image?\inline&space;O(k)>), where n is the length of array and k is the number of closest points to the origin we need to return.
