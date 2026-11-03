class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not len(stack) or stack.pop() != mapping[c]:
                    return False
        return len(stack) == 0

        