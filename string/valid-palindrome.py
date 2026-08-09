class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalpha())
        t = s[::-1]
        if s == t:
            return True
        else:
            return False
        