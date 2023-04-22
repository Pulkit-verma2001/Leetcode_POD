class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
        def solve(i,j):
            if i>j : return 0

            if dp[i][j]!=-1 : return dp[i][j] # returning answer is already present in dp table

            a,b=0,0
            if s[i]==s[j]: # case when end characters are same 
                a=solve(i+1,j-1) # if this case then we don't need to add any character
            else:
                b=1+min(solve(i+1,j),solve(i,j-1)) 
                # if end characters are not same then we have to add a character
                # for adding any character we have two option : 
                # 1- adding character at   front, 
                # 2- adding character at end
                # so we will take min of both the cases and add one 
                #to it to denote a addition of character.

            dp[i][j]=a+b # storing the result in dp table

            return a+b
        return solve(0,n-1)