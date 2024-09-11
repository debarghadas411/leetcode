class Solution:
    def myAtoi(self, s: str) -> int:
        pos=0
        n=len(s)
        if n==0:
            return 0
        output=0
        while pos<n and s[pos]==' ':
            pos+=1
        sign=1
        if pos<n and s[pos]=='-':
            sign=-1
            pos+=1
        elif pos<n and s[pos]=='+':
            pos+=1
        while pos<n:
            digit=-1
            if s[pos]=='0':
                digit=0
            elif s[pos]=='1':
                digit=1
            elif s[pos]=='2':
                digit=2
            elif s[pos]=='3':
                digit=3
            elif s[pos]=='4':
                digit=4
            elif s[pos]=='5':
                digit=5
            elif s[pos]=='6':
                digit=6
            elif s[pos]=='7':
                digit=7
            elif s[pos]=='8':
                digit=8
            elif s[pos]=='9':
                digit=9
            if digit==-1:
                break
            output=output*10+digit
            pos+=1
        output=output*sign
        if output>((2**31)-1):
            output=2**31-1
        elif output<-1*(2**31):
            output=-1*(2**31)
        return output
        