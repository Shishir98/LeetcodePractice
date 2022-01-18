class Solution:
    def thirdMax(self, nums: List[int]) -> int:
      
      # Easy solution using sets and basic If else statement
      
        set1 = set(nums)
        nums2 = list(set1)
        nums2.sort()
        if len(nums2) >= 3:
            return nums2[-3]
        elif len(nums2) == 2:
            return max(nums2)
        elif len(nums2) == 1:
            return max(nums2)
        else: 
            return "error"
            
        
