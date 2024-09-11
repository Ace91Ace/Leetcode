class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:  
        start = bin(start)[2:]  
        goal = bin(goal)[2:]  

        max_length = max(len(start), len(goal))  
        start = start.zfill(max_length)  
        goal = goal.zfill(max_length)
        count = 0  

        for i in range(max_length):  
            if goal[i] != start[i]:  
                count += 1  

        return count