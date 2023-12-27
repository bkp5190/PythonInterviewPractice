from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = [] # Will hold [value, index]

    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stack_val, stack_index = stack.pop()
            temperatures[stack_index] = index - stack_index
        stack.append([temp, index])
        temperatures[index] = 0

    return temperatures



assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert dailyTemperatures([30,60,90]) == [1,1,0]
