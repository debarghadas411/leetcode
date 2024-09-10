class Solution:
    def reverse(self, x: int) -> int:
        if x==0: 
            return 0
        sign=x//abs(x)
        num=abs(x)
        rev=0
        while num>0:
            rev=rev*10+(num%10)
            num=num//10
        print(rev)
        if rev>((2**31)-1):
            return 0
        else:
            return sign*rev

        