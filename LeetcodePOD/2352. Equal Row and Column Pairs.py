class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dict=defaultdict(int)
        dr=defaultdict(list)
        dc=defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid)):
                ele=grid[i][j]
                dr[i]+="@"+str(ele)
                dc[j]+="@"+str(ele)
        
        for s in dr.values():
            s1="".join(s)
            dict[s1]+=1
        ans=0

        for s in dc.values():
            s1="".join(s)
            if dict[s1]!=0:
                ans+=dict[s1]
        return ans