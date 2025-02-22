class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        for ch in expression:
            if ch==',':
                continue
            if ch==')':
                result=[]
                while stack[-1]!='(':
                    result.append(stack.pop())

                stack.pop()
                operator=stack.pop()
                stack.append(self.solve_func(result,operator))
            else:
                stack.append(ch)
        return True if stack[0]=='t' else False

    def solve_func(self,result,operator):
        if operator=='!':
            return 't' if result[0]=='f' else 'f'

        if operator=='&':
            for ch in result:
                if ch=='f':
                    return 'f'

            return 't'

        if operator=='|':
            for ch in result:
                if ch=='t':
                    return 't'

            return 'f'



