'''Write a function that takes in an integer array (0/1) of flowers in a bed and if you can plant
   n numbers of flowers. No two flowers can be next to each other.'''

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        plantable = 0

        for i in flowerbed:
            if i == 1:
                counter = 0
            else:
                counter += 1
                if counter == 3:
                    plantable += 1
                    counter = 0

        return plantable == n
    
solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(solution.canPlaceFlowers([1, 0, 1, 0, 1, 0, 0, 0], 2))
print(solution.canPlaceFlowers([1, 0, 1, 0, 1, 0, 0, 0], 1))
print(solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0, 0], 2))
