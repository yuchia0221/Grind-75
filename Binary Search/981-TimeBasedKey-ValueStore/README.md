# Time Based Key-Value Store

Problem can be found in [here](https://leetcode.com/problems/time-based-key-value-store)!

### [Solution](/Binary%20Search/981-TimeBasedKey-ValueStore/solution.py): Hash Table + Binary Search

Explanation: To achieve great time complexity, we can use a hash table to quickly retrieve the key's value in constant time. However, there may be multiple values with different time stamps for each key. We can definitely search linearly to find the largest timestamp by iterating the whole array. To improve the running speed, we can instead perform binary search to help us to find the returned value quickly.

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
