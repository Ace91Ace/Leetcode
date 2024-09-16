class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mint = []

        for i in timePoints:
            mint.append(60*int(i[0:2]) + int(i[3:]))
        print(mint)
        
        
        mint.sort()  
        mind = float('inf')  
        
        for i in range(len(mint)):  
            curr = mint[(i + 1) % len(mint)] - mint[i]
            print(i ," ", curr)

            if curr < 0:  
                curr += 1440 
            mind = min(mind, curr)  

        return mind
        