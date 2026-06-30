class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=set()
        l=0
        m=0
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l+=1
            c.add(s[r])
            m=max(m,r-l+1)    

        return m    