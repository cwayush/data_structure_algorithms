from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        size = len(lcp)
        result = [""] * size
        ch_code = ord('a')

        for start in range(size):
            if result[start] == "":
                if ch_code > ord('z'):
                    return ""

                current_char = chr(ch_code)
                result[start] = current_char

                for nxt in range(start + 1, size):
                    if lcp[start][nxt] > 0:
                        result[nxt] = current_char

                ch_code += 1

        for x in range(size - 1, -1, -1):
            for y in range(size - 1, -1, -1):

                if result[x] != result[y]:
                    if lcp[x][y] != 0:
                        return ""
                else:
                    if x == size - 1 or y == size - 1:
                        if lcp[x][y] != 1:
                            return ""
                    else:
                        if lcp[x][y] != lcp[x + 1][y + 1] + 1:
                            return ""

        return "".join(result)