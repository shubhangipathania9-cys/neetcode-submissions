class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(nums)
        count=1
        d=1
        print(s)
        if nums==[]:
            return 0

        for i in range (len(s)-1):
            if s[i]==s[i+1]:
                continue
            elif s[i+1]==s[i]+1:
                count+=1
            else:
                d=max(count,d)
                count=1
        return max(count,d) 
               
        