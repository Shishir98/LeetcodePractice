class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #hardbreach method, 2 for loops O(n^2)
        
        def hardBreach(self, nums, target):
            i=0
            j=0
            for i in range(-1,len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] ==  target:
                        return(i,j)
        return hardBreach(self,nums,target)
    
    class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Dictionary Method O(n)
        
        def dictMethod(self, nums, target):
            dic = {}
            for i, n in enumerate(nums): 
                if n in dic:
                    return [dic[n], i]
                dic[target-n] = i
        return dictMethod(self,nums, target)
