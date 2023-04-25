class SmallestInfiniteSet:
    def __init__(self):
        self.next_num = 1
        self.min_heap = []        

    def popSmallest(self) -> int:
        if self.min_heap:
            return heappop(self.min_heap)
    
        num_to_return = self.next_num
        self.next_num += 1
        return num_to_return
        

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.min_heap:
            heappush(self.min_heap, num)