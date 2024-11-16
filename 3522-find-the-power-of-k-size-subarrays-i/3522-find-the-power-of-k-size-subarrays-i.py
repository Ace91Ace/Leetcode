from typing import List  

class Solution:  
    def resultsArray(self, nums: List[int], k: int) -> List[int]:  
        maxi = max(nums[0:k])  
        res = []  
        sub = []  
        
        # Calculate the differences to create the sub list  
        for i in range(len(nums) - 1):  
            if nums[i + 1] - nums[i] == 1:  
                sub.append(1)  
            else:  
                sub.append(0)  
        
        # Initial check to set the first result based on the first k elements  
        if sum(sub[0:k-1]) == (k - 1):  
            res.append(maxi)  
        else:  
            res.append(-1)  

        n = len(nums)  

        # Iterate through the array with a sliding window  
        for i in range(n - k + 1):  
            # Calculate the maximum in the current sliding window  
            if i == 0:  
                current_max = maxi  # Use the pre-computed maximum for the first window  
            else:  
                # Update the sliding window maximum accordingly  
                current_max = max(nums[i:i + k])  # Take the max of the current window  

            # Check if the condition satisfies for the sub array  
            if sum(sub[i:i + (k - 1)]) == (k - 1):  
                res.append(current_max)  
            else:  
                res.append(-1)  

        return res[1:]