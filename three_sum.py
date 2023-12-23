from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:

    # Sort the incoming list in O(n * log(n))
    nums.sort()

    # Create a result array
    res = []

    # Iterate over each number
    for i, n in enumerate(nums):
        # Same as the previous element, need to skip duplicates
        if i > 0 and n == nums[i - 1]:
            continue

        # Create the left and right pointers
        l, r = i + 1, len(nums) - 1

        while l < r:
            three_sum = nums[l] + nums[r] + n

            # Too large
            if three_sum > 0:
                r -= 1

            # Too small
            elif three_sum < 0:
                l += 1

            # We found a valid sum
            else:
                res.append([nums[l], n, nums[r]])
                l += 1

                # Account for duplicates by continually updating
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    # Return final result
    return res


assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[0,-1,1]]
