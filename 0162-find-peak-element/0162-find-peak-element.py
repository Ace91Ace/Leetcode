class Solution:  
    def findPeakElement(self, nums: List[int]) -> int:  
        s = 0  
        n = len(nums) - 1  

        while s < n:  
            mid = s + (n - s) // 2  
            if nums[mid] < nums[mid + 1]:  
                s = mid + 1  
            else:  
                n = mid  

        return s