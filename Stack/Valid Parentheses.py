class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)

            else:
                if stack:
                    top = stack[-1]
                    if (char == ')' and top == '(') or (char == '}' and top == '{') or (char == ']' and top == '['):
                        stack.pop()

                    else:
                        return False
                else:
                    return False

        if not stack:
            return True

        return False
        