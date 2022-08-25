# Find Median from Data Stream

Problem can be found in [here](https://leetcode.com/problems/find-median-from-data-stream)!

### [Solution](/Heap/295-FindMedianfromDataStream/solution.py): Heap

```python
class MedianFinder:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) < len(self.max_heap):
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            heappush(self.max_heap, -heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]
```

Time Complexity: ![O(lgn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>) for adding new number and ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) for finding the median number, Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the number of numbers.
