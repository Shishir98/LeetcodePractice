class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
      #solution attempted using sets method.
      
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
