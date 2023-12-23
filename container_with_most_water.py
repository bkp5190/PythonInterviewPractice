from typing import List


def maxArea(height: List[int]) -> int:
    # Two pointer approach
    res = 0

    l, r = 0, len(height) - 1

    while l < r:
        # Calculate current area
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        # Update pointers
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res


assert maxArea([1,8,6,2,5,4,8,3,7]) == 49

assert maxArea([1,1]) == 1
