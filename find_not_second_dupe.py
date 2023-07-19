# Given an array of integers, find the integer that is not repeated twice
# There will always be one integer that is not repeated.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor
    
# When you XOR an int ^ int = 0
# When you XOR an int ^ 0 = int
# O(n) Time, O(1) Space