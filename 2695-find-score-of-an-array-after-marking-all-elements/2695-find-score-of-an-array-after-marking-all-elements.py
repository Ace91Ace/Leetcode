import heapq  
from typing import List  

class Solution:  
    def findScore(self, nums: List[int]) -> int:  
        n = len(nums)  
        res = 0  
        marked = set()  
        min_heap = []  

        for i in range(n):  
            heapq.heappush(min_heap, (nums[i], i))  

        while len(marked) < n:  
            while min_heap:  
                value, i = heapq.heappop(min_heap)  
                if i not in marked:  
                    break  
            else:  
                break  

            marked.add(i)  
            if i - 1 >= 0: marked.add(i - 1)  
            if i + 1 < n: marked.add(i + 1)  
            res += value  

        return res