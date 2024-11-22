class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]

        l = max(len(goal),len(start)) - min(len(goal),len(start))

        if len(goal) > len(start):  
            start = '0' * l + start  
        elif len(goal) < len(start):  
            goal = '0' * l + goal

        count = 0
        for i in range(len(start)):
            if goal[i] != start[i]:
                count += 1

        return count
        
