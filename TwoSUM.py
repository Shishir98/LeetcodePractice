class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #hardbreach method, 2 for loops
        
        def hardBreach(self, nums, target):
            i=0
            j=0
            for i in range(-1,len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] ==  target:
                        return(i,j)
        return hardBreach(self,nums,target)
      
 
                
