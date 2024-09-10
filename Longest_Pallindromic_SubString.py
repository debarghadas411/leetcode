class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return s
        elif n==2 and s[0]==s[1]:
            return s
        elif n==2 and s[0]!=s[1]:
            return s[0]
        else:
            lpss=s[0]
            for pos in range(n):
                i=pos-1
                j=pos+1
                temp=s[pos]
                while i>=0 and j<n and s[i]==s[j]:
                    temp=s[i:j+1]
                    i-=1
                    j+=1
                if len(lpss)<len(temp):
                    lpss=temp
            for pos in range(n-1):
                if s[pos]==s[pos+1]:
                    i=pos-1
                    j=pos+2
                    temp=s[pos:pos+2]
                    while i>=0 and j<n and s[i]==s[j]:
                        temp=s[i:j+1]
                        i-=1
                        j+=1
                    if len(lpss)<len(temp):
                        lpss=temp
            return lpss
                    

        