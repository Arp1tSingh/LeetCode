class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            elif ch == "-":
                y, x = stack.pop(), stack.pop()
                stack.append(x - y)
            elif ch == "/":
                y, x = stack.pop(), stack.pop()
                stack.append(int(x / y))
            else:
                stack.append(int(ch))
        
        return stack.pop()