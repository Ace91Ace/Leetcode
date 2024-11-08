from typing import List  

class Solution:  
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:  
        l = (1 << maximumBit) - 1  
        res = []  
        xor = 0  
        n = len(nums)  

        for num in nums:  
            xor ^= num  

        for i in range(n):  
            res.append(xor ^ l)  
            xor ^= nums[n - 1 - i]  

        return res