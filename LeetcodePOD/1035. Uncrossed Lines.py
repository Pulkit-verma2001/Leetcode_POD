class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        dp=[[-1 for _ in range(n2+1)] for _ in range(n1+1)]
        def solve(i,j):
            if i==n1 or j==n2 : return 0
            if dp[i][j]!=-1 : return dp[i][j]
            a1,a2=0,0

            if nums1[i]==nums2[j]:
                a1+=1+solve(i+1,j+1)
            else:
                a2=max(solve(i+1,j),solve(i,j+1))

            dp[i][j]=max(a1,a2)
            return dp[i][j]
        return solve(0,0)
    