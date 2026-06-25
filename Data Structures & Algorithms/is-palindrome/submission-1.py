class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=""
        l=""
        for i in s:
            if i == " " or i in "!@#$%^&*()_+[]\{}|;':,./<>?-+":
                continue
            else:     
                d+=i

        for i in range (len(d)-1,-1,-1):
            l+=d[i]

        print(l)
        print(d)    

        if d.lower()==l.lower():
            return True

        else:
            return False         