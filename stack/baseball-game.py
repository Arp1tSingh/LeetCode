class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for x in operations:
            if x.lstrip('-').isdigit():
                stack.append(int(x))

            elif x == 'C':
                stack.pop()

            elif x == 'D':
                stack.append(stack[-1] * 2)

            elif x == '+':
                stack.append(stack[-1] + stack[-2])

        return sum(stack) 