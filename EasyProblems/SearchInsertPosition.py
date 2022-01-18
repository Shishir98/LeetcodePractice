class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
      
      #Using Linear Search-- 
      
      
        for num in nums:
            if target == num:
                return nums.index(target)
            elif target != num:
                nums.append(target)
                nums.sort()
                return nums.index(target)
        
