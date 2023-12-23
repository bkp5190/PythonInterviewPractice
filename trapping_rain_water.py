from typing import List

def trap(height: List[int]) -> int:
    # Edge case to check if the array is empty
    if not height:
        return 0

    # Create left and right pointer at beginning and end of array
    l, r = 0, len(height) - 1

    # Result value
    res = 0

    # Set the maximum heights encountered to current pointer locations
    l_max, r_max = height[l], height[r]

    # Iterate until the left and right pointers meet
    while l < r:
        # If the left maximum is less, increment the left pointer
        if l_max < r_max:
            l += 1
            # Check the new maximum
            l_max = max(l_max, height[l])

            # Add to the result
            res += l_max - height[l]

        else:
            r -= 1
            # Check the new maximum
            r_max = max(r_max, height[r])

            # Add to the result
            res += r_max - height[r]

    return res



assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

assert trap([4,2,0,3,2,5]) == 9
