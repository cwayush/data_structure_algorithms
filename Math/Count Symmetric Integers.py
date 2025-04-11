class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            s = str(i)
            length = len(s)
            if length%2!=0:
                continue

            n = length//2
            
            left_sum = sum(int(d) for d in s[:n])
            right_sum = sum(int(d) for d in s[n:])

            if left_sum == right_sum:
                count+=1

        return count

# Approach-1 (Math)
# T.C : O(n∗log(high))
# S.C : O(1)  

sol=Solution()

low = 1
high = 100
print(sol.countSymmetricIntegers(low,high))
