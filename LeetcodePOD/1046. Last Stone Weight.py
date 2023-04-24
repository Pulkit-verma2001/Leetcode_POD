class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-i for i in stones]
        heapify(heap)
        while len(heap)>1:
            y=abs(heappop(heap))
            x=abs(heappop(heap))
            if x==y : continue
            heappush(heap,-1*(y-x))
        if len(heap)==0 : return 0
        return abs(heap[0]) 