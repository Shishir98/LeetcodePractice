class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x=[]
        for num in nums:
            y =num**2
            x.append(y)
            x.sort()
        return x
            
