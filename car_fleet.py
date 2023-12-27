from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    # Create a stack to hold the times taken to reach the target
    stack = []

    # Zip together the position and speeds into another list
    pairs = [[p, s] for p, s in zip(position, speed)]

    # Iterate through the pairs in reverse sorted order
    for p, s in sorted(pairs)[::-1]:
        # Calculate the time and add to the stack
        stack.append((target - p) / s)
        # The times overlap, so we can combine
        if len(stack) >= 2 and stack[-2] >= stack[-1]:
            # Remove the element
            stack.pop()
    # Return the final length of the stack
    return len(stack)


assert carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
