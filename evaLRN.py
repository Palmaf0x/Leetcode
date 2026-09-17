class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))  # Truncates toward zero
            else:
                stack.append(int(token))

        return stack[0]