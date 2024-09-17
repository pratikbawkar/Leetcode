# Given two binary strings a and b, return their sum as a binary string. 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_int = int(a, 2) + int(b, 2)
        return bin(sum_int)[2:]

solution=Solution()
print(solution.addBinary("11", "1"))    
print(solution.addBinary("1010", "1011"))
