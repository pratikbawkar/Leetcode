#this is a classic palindrome solution
# pushing through VS code now as learning to intergrate my github in vscode and push directly through VS code


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)

        return s == s[::-1]
