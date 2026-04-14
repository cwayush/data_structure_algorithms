class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        res = []

        for i in range(n):
            deg = sum(matrix[i])
            res.append(deg)

        return res