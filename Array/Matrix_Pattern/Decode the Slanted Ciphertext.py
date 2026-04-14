class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)

        cols = n // rows

        matrix = []
        index = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(encodedText[index])
                index += 1

            matrix.append(row)

        result = []

        for col in range(cols):
            i,j = 0,col

            while i<rows and j<cols:
                result.append(matrix[i][j])
                i+=1
                j+=1

        return ''.join(result).rstrip()