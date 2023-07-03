# Given an array of sorted distinct elements, find the index of a target value.
# If the value is not in the array, return the index to where it should be inserted.
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Sorted array, distinct
        # Binary search, return index
        # O(logn) is Binary Search

        first, last = 0, len(nums) - 1
        while (first <= last):
            mid = (first + last) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                first = mid + 1
            else:
                last = mid - 1
        return first
    

solution = Solution()
print(solution.searchInsert([1, 2, 3, 4, 5], 3))
print(solution.searchInsert([1, 2, 3, 4, 5, 10, 20], 6))
print(solution.searchInsert([1, 2, 3, 4, 5, 10, 20], 20))