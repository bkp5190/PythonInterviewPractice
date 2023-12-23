from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    output = [1] * len(nums)

    # First pass through, store prefix in output

    prefix = 1

    for i, num in enumerate(nums):
        output[i] = prefix
        prefix = num * prefix

    # Second pass through postfix
    postfix = 1

    for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * postfix
        postfix = nums[i] * postfix

    return output


assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
