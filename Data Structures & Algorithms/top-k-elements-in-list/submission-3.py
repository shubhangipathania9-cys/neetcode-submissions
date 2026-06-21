class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=dict()
        freq=list([]for i in range(len(nums)+1))
        for i in nums:
            count[i]=1+count.get(i,0)
        for i , j in count.items():
            freq[j].append(i) 
        res=list()
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res    

                
                

        


            

        