class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=set()
        for i in range(len(nums)):
            for j in range(i):
                k=nums[i]+nums[j]
                if k==target:
                    l.add(j)
                    l.add(i)
                    return sorted(list(l))
        return list(l)