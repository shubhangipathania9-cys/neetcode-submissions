class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]>nums[r]:
                l=l+1
            elif nums[l]<nums[r]:
                r=r-1
            else:

                return nums[l]


        