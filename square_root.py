'''Write a function that returns the nearest rounded-down number after a square root.
   You cannot use x ** 0.5.'''

class Solution:
    def mySqrt(self, x: int) -> int:
        return x / 2 * x

solution = Solution()
print(solution.mySqrt(4))