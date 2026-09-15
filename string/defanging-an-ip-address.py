class Solution:
    def defangIPaddr(self, address: str) -> str:
         na = address.replace(".","[.]")
         return na