class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        l,r=0,len(nums1)-1
        nums=sorted(nums1)
        print(nums)
        if len(nums)%2 == 0:
            j=len(nums)//2
            return (nums[j] + nums[j-1])/2
        else:
            m=(l+r)//2
            return nums[m]

        
        