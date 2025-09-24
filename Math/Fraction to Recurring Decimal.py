class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)

        result.append(str(numerator // denominator))
        
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, "(")
                result.append(")")
                break
            
            remainder_map[remainder] = len(result)
            
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator
        
        return "".join(result)

# Approach-1 (HashMap)
# T.C : O(n)
# S.C : O(n)

sol = Solution()
numerator = 4
denominator = 333
print(sol.fractionToDecimal(numerator,denominator))