class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        result = ["a"] * (len1 + len2 - 1)
        is_fixed = [False] * (len1 + len2 - 1)

        for i, flag in enumerate(str1):
            if flag == "T":
                for j, char in enumerate(str2, i):
                    if is_fixed[j] and result[j] != char:
                        return ""
                    result[j] = char
                    is_fixed[j] = True

        for i, flag in enumerate(str1):
            if flag == "F":
                if any(str2[j - i] != result[j] for j in range(i, i + len2)):
                    continue

                for j in range(i + len2 - 1, i - 1, -1):
                    if not is_fixed[j]:
                        result[j] = "b"
                        break
                else:
                    return ""

        return "".join(result)