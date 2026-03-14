from collections import defaultdict

class Solution:
    def user_logic(self,n, arr):
        mapp = defaultdict(int)
        new_arr = sorted(arr)

        for i,num in enumerate(new_arr):
            mapp[num] = i

        sanity = 0
        for i,num in enumerate(arr):
            sanity += (i + mapp[num])

        return sanity

sol=Solution()

n = 6
arr = [2,1,3,2,3,1]
print(sol.user_logic(n,arr))