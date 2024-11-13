from typing import List  
import bisect  

class Solution:  
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:  
        nums.sort()  
        count = 0  
        n = len(nums)  

        for i in range(n):  
            # Calculate the target values for binary search  
            target_lower = lower - nums[i]  
            target_upper = upper - nums[i]  
            
            # Use bisect to find the valid range  
            left_index = bisect.bisect_left(nums, target_lower, i + 1)  
            right_index = bisect.bisect_right(nums, target_upper, i + 1)  
            
            # The number of valid pairs for this i is the difference of indices  
            count += (right_index - left_index)  

        return count