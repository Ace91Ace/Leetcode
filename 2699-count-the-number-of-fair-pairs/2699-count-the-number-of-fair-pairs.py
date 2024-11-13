from typing import List  

class Solution:  
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:  
        nums.sort()  
        count = 0  
        n = len(nums)  
        
        # We will use a single loop for left pointer  
        for left in range(n):  
            # Create a range for right pointer  
            low = left + 1  # right pointer must always be to the right of left pointer  
            high = n  
            
            # Find the first position `high` where pair is greater than upper  
            while low < high:  
                mid = (low + high) // 2  
                if nums[left] + nums[mid] > upper:  
                    high = mid  
                else:  
                    low = mid + 1  
            
            # Now, `low` is the first index where the sum exceeds `upper`  
            right_high = low  
            
            # Find the position `high` where pair is less than lower  
            low = left + 1  
            high = n  
            
            while low < high:  
                mid = (low + high) // 2  
                if nums[left] + nums[mid] < lower:  
                    low = mid + 1  
                else:  
                    high = mid  
            
            # Now `low` is the first index where the sum meets or exceeds `lower`  
            right_low = low  
            
            # Count pairs in the valid range  
            count += (right_high - right_low)  
        
        return count