class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count,window={},{}
        for c in t:
            count[c]=count.get(c,0)+1
            have,need=0,len(count)
            res,reslen=[-1,-1],float("infinity")
            l=0
        for r in range (len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in count and window [c]==count[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=(r-l+1)
                    
                window[s[l]] -= 1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen != float("infinity") else""