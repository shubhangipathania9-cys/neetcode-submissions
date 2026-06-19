class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=list()
        e=list()
        for i in s:
            d.append(i)

        for j in t:
            e.append(j)

        if sorted(d)==sorted(e):
            return True
        else:
            return False         

        