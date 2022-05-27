# Trapping Rain Water

Problem can be found in [here](https://leetcode.com/problems/trapping-rain-water)!

### [Solution1](/Stack/42-TrappingRainWater/solution1.py): Dynamic Programming

```python
def trap(height: List[int]) -> int:
    volumne = 0
    left_max, right_max = [0], [0]*len(height)
    left_max[0], right_max[-1] = height[0], height[-1]

    for i in range(1, len(height)):
        left_max.append(max(left_max[-1], height[i]))

    for i in range(len(height)-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    for i in range(len(height)):
        volumne += min(left_max[i], right_max[i]) - height[i]

    return volumne
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

### [Solution2](/Stack/42-TrappingRainWater/solution2.py): Two Pointers

```python
def trap(height: List[int]) -> int:
    left, right = 0, len(height)-1
    left_max = right_max = volumne = 0
    while left <= right:
        if left_max <= right_max:
            volumne += max(left_max - height[left], 0)
            left_max = max(left_max, height[left])
            left += 1
        else:
            volumne += max(right_max - height[right], 0)
            right_max = max(right_max, height[right])
            right -= 1

    return volumne
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [Solution3](/Stack/42-TrappingRainWater/solution3.py): Stack

```python
def trap(height: List[int]) -> int:
    stack = []
    volumne = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            candidate = height[stack.pop()]
            if stack:
                bounded_height = min(height[i], height[stack[-1]]) - candidate
                width = i - stack[-1] - 1
                volumne += bounded_height * width

        stack.append(i)

    return volumne
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
