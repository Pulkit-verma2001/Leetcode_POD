class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        dict={}
        def solve(ind,end,k):
            if ind>=len(events) or k<=0 : return 0

            if (ind,end,k) in dict : return dict[(ind,end,k)]
            s,e,v=events[ind]
            a1=0
            if s>end :
                a1=v+solve(ind+1,e,k-1)
            a2=solve(ind+1,end,k)

            dict[(ind,end,k)]=max(a1,a2)
            return max(a1,a2)
        return solve(0,-1,k)