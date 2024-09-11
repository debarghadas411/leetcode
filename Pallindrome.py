class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=x
        output=0
        while num>0:
            output=output*10+(num%10)
            num=num//10
        if output==x:
            return True
        else:
            return False

        