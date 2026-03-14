class Solution:
    def isSubsetSumRec(self, arr, n, sum):
        if sum == 0:
            return True 
        if n == 0:
            return False

        if arr[n - 1] > sum:
            return self.isSubsetSumRec(arr, n - 1, sum)


        return (self.isSubsetSumRec(arr, n - 1, sum) or 
                self.isSubsetSumRec(arr, n - 1, sum - arr[n - 1]))

    def isSubsetSum(self, arr, sum):
        
        return self.isSubsetSumRec(arr, len(arr), sum)
