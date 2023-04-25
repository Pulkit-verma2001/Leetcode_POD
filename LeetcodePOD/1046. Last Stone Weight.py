import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            y=abs(heapq.heappop(heap))
            x=abs(heapq.heappop(heap))
            if x==y : continue
            heapq.heappush(heap,-1*(y-x))
        if len(heap)==0 : return 0
        return abs(heap[0]) 