class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        leftclosest_r  = [-1]*n
        rightclosest_l = [-1]*n
        for i,char in enumerate(dominoes):
            if char == 'R':
                leftclosest_r[i] = i
            elif char == '.' and i>0:
                leftclosest_r[i] = leftclosest_r[i-1] 

        for i in range(n-1,-1,-1):
            if dominoes[i] == 'L':
                rightclosest_l[i] = i
            elif dominoes[i] == '.' and i<n-1:
                rightclosest_l[i] = rightclosest_l[i+1]

        result = []
        for i in range(n):
            left = leftclosest_r[i]
            right = rightclosest_l[i]

            disLeftR = abs(i - left) if left != -1 else float('inf')
            disRightL = abs(i - right) if right != -1 else float('inf')

            if disLeftR == disRightL:
                result.append('.')
            elif disLeftR < disRightL:
                result.append('R')
            elif disRightL < disLeftR:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)

# Approach-1 (Hashmap)
# T.C : O(n)
# S.C : O(n)

sol=Solution()

dominoes = ".L.R...LR..L.."
print(sol.pushDominoes(dominoes))