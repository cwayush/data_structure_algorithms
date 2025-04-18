class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        say = self.countAndSay(n-1)

        result = ""
        i=0
        while i < len(say):
            ch = say[i]
            count = 1
            while i < len(say) - 1 and say[i] == say[i + 1]:
                count += 1
                i += 1
            result += str(count) + ch
            i += 1

        return result
    
sol=Solution()

n=5
print(sol.countAndSay(n))
        
        # 1 = 1
        # 2 = 11
        # 3 = 21
        # 4 = 1211
        # 5 = 111221
        # 6 = 312211
        # 7 = 13112231
        # 8 = 111321221311