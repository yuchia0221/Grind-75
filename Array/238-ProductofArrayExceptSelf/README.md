# Product of Array Except Self

Problem can be found in [here](https://leetcode.com/problems/product-of-array-except-self)!

### [Basic Solution](/Array/238-ProductofArrayExceptSelf/solution1.py): Prefix Product & Suffix Product

```python
def productExceptSelf(nums: List[int]) -> List[int]:
    prefix_poduct, output_list = 1, []
    for number in nums:
        output_list.append(prefix_poduct)
        prefix_poduct *= number

    suffix_poduct = 1
    for i in range(len(nums) - 1, -1, -1):
        output_list[i] *= suffix_poduct
        suffix_poduct *= nums[i]

    return output_list
```

Explanation: Since we only iterate _nums_ twice and all of operations inside loops are performed in constant time, so the algorithm runs in O(2\*n) = O(n) time. Suppose _nums_ = [a, b, c, d]. After first loop, we will get output_list = [1, a, ab, abc]. Noted that the value of the last element is exactly the product of array except self. With this in mind, we only need to iterate _nums_ backward to calculate the value of each element via suffix_poduct. In the second for-loop, when i = len(nums)-1 (the last element), output_list\[i] is exactly output_list and suffix_product = 1 \* d. When i=len(nums)-2, the value will be output_list\[i] \* suffix_product = ab \* d = abd. As as result, we get an array with its value is the product of array except self.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

> Please noted that the output array does not count as an extra space for space complexity analysis!

### [Improved Solution](/Array/238-ProductofArrayExceptSelf/solution2.py)

```python
def productExceptSelf(nums: List[int]) -> List[int]:
    output_list = [1] * len(nums)
    prefix_poduct = suffix_poduct = 1
    for index, number in enumerate(nums):
        output_list[index] *= prefix_poduct
        prefix_poduct *= number
        output_list[-1 - index] *= suffix_poduct
        suffix_poduct *= nums[-1 - index]

    return output_list
```

Notes: Optimizing the algorithm for needing only for-loop.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
