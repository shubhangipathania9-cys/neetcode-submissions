class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        o=[]
        for i in range (len(temperatures)):
            c=0
            d=temperatures[i:]
            for j in range(len(d)):
                if d[j]>temperatures[i]:
                    c+=j
                    break
                else:
                    continue
            o.append(c)
        return o

        