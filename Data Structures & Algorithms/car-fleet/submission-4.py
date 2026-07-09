class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        stack2=[]
        stack3=[]
        for i in range (len(speed)):
            b=speed[i]
            a=position[i]
            stack.append([a,b])
        for a,b in sorted(stack)[::-1]:
            stack2.append((target-a)/b)
            if len(stack2)>=2 and stack2[-1]<=stack2[-2]:
                stack2.pop()
    
        return len(stack2)

            
        