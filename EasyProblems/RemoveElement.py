class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      #https://leetcode.com/problems/remove-element/
        y= 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[y] = nums[i]
                y += 1
        return y  
