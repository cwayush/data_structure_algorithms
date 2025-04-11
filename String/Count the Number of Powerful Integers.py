class Solution:
    def solve(self,strr,input_str,limit):
        if len(strr)<len(input_str):
            return 0

        count = 0
        remain_len = len(strr) - len(input_str)

        for i in range(remain_len):
            digit = int(strr[i])
            if digit<=limit:
                count+=digit*pow(limit+1,remain_len-i-1)
            else:
                count+=pow(limit+1,remain_len-i)
                return count

        if strr[-len(input_str):]>=input_str:
            count+=1 
        return count

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        start_str = str(start-1)
        finish_str = str(finish)
        return self.solve(finish_str,s,limit) - self.solve(start_str,s,limit)
    

sol=Solution()

start = 1
finish = 6000
limit = 4
s = "124"
print(sol.numberOfPowerfulInt(start,finish,limit,s)) # Output: 5
