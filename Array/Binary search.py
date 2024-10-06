class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg=0
        end=len(nums)-1
        while beg<=end:
            mid=int((beg+end)/2)
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                beg=mid+1
            else:
                end=mid-1
        return -1