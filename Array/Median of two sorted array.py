class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums=sorted(nums1)
        n=len(nums1)
        if n%2==0:
            return float((nums[int(n/2)-1]+nums[int(n/2)])/2)
        else:
            return float(nums[int(n/2)])