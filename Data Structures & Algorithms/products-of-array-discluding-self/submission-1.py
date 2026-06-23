import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        o=[0]*(len(nums))
        for i in range (len(nums)):
            s=nums[:i]
            f=nums[(i+1):]
            res=math.prod(s)*math.prod(f)
            print (res)
            o[i]+=res
        return o    