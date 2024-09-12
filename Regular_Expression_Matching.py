class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(p)
        n=len(s)
        D=[[False for i in range(n+1)] for j in range(m+1)]
        D[0][0]=True
        for i in range(1,m+1):
            if p[i-1]=='*':
                D[i][0]=D[i-2][0]
        for j in range(n):
            for i in range(m):
                
                if p[i]=='*' and (p[i-1]==s[j] or p[i-1]=='.'):
                    D[i+1][j+1]=D[i+1][j] or D[i-1][j+1]
                elif p[i]=='*':
                    D[i+1][j+1]= (D[i][j+1] or D[i-1][j+1])
                elif p[i]==s[j] or p[i]=='.':
                    D[i+1][j+1]=D[i][j]
                print(i,j,p[i],s[j],D[i+1][j+1])
        print(D)
        return D[m][n]