# The isBadVersion API is defined as followed
def isBadVersion(version: int) -> bool:
    ...


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left+right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
