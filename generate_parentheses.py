from typing import List


def generateParenthesis(n: int) -> List[str]:
    # Backtracking and stack

    stack = []
    res = []

    def backtrack(open, closed):
        if open == closed == n:
            # Base case return result
            res.append("".join(stack))

        if open < n:
            stack.append('(')
            backtrack(open + 1, closed)
            stack.pop()

        if closed < open:
            stack.append(')')
            backtrack(open, closed + 1)
            stack.pop()


    backtrack(0, 0)
    return res


assert generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
assert generateParenthesis(1) == ["()"]
