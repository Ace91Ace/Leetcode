class Solution:  
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:  
        nums.sort()  
        count = 0  
        n = len(nums)  
        
         
        for left in range(n):  
            low = left + 1 
            high = n  
             
            while low < high:  
                mid = (low + high) // 2  
                if nums[left] + nums[mid] > upper:  
                    high = mid  
                else:  
                    low = mid + 1  
            right_high = low  
            
           
            low = left + 1  
            high = n  
            
            while low < high:  
                mid = (low + high) // 2  
                if nums[left] + nums[mid] < lower:  
                    low = mid + 1  
                else:  
                    high = mid  
            
            right_low = low  
            
            count += (right_high - right_low)  
        
        return count