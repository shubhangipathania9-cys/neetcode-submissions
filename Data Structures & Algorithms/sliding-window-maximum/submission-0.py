class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h=[]
        for i in range (len(nums)-k+1):
            l=nums[i:i+k]
            h.append(max(l))
        return h
        

        