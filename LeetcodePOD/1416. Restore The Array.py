class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n=len(s)
        M=10**9+7
        dp={}
        def solve(ind,prev):
            if ind>=n:
                return 1
        
            ans=0
            curr=int(s[ind])
            if curr!=0:
                if ind in dp:
                    ans+=dp[ind]
                else:
                    ans+=solve(ind+1,curr)
                    dp[ind]=ans%M
            prev=prev*10+curr
            if prev<=k:
                ans+=solve(ind+1,(prev))

            return ans
        return solve(1,int(s[0]))%M