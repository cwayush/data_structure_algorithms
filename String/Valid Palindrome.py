class Solution:
    def isPalindrome(self, s: str) -> bool:
       new_str = ''.join(char.lower() for char in s if char.isalnum()) 
       return new_str == new_str[::-1]