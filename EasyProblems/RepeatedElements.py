class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x = len(nums)//2
        print(x)
        for num in nums:
            counter = nums.count(num)
            if counter == x:
                return num
