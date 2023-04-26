class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        num=list(map(int,num))
        
        while len(num)!=1:
            num=sum(num)
            num=str(num)
            num=list(map(int,num))
        return num[0]