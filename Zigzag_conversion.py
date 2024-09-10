class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output=''
        n=len(s)
        if numRows==1:
            return s
        if n<=numRows:
            return s
        for r in range(numRows):
            up1=(numRows-r-1)*2
            up2=r*2
            pos=r
            output+=s[pos]
            while pos<n:
                if up1>0 and pos+up1<n:
                    output+=s[pos+up1]
                pos+=up1
                if up2>0 and pos+up2<n:
                    output+=s[pos+up2]
                pos+=up2
        return output