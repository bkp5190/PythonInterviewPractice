# Write a function which will calculate if kid[i] will have the most candies
# in the group if given n extraCandies. Return a boolean array mapping to each kid.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maximum = max(candies)
        for i, n in enumerate(candies):
            value = n + extraCandies
            if (value >= maximum):
                res.append(True)
            else:
                res.append(False)
        return res