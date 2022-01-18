class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      
      #Easy solution using .count method.
      
        for num in nums:
            x = nums.count(num)
            if x == 1:
                return(num)
