class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        l=len(group)
        dp=[[[-1 for _ in range(n+1)] for _ in range(minProfit+1)] for _ in range(l+1)]
        def solve(i,p,ng):
            if ng>n : return 0
            if i>=l:
                if p>=minProfit and ng<=n:
                    return 1
                return 0
            if dp[i][p][ng]!=-1 : return dp[i][p][ng]
            n1=solve(i+1,p,ng) # not pick
            n2=solve(i+1,min(minProfit,p+profit[i]),ng+group[i]) # pick
            dp[i][p][ng]=n1+n2
            return n1+n2
        
        return solve(0,0,0)%(10**9+7)