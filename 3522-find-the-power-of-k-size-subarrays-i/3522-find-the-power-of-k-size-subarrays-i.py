class Solution:  
    def resultsArray(self, nums: List[int], k: int) -> List[int]:  
        maxi = max(nums[0:k])  
        res = []  
        sub = []  
        
        for i in range(len(nums) - 1):  
            if nums[i + 1] - nums[i] == 1:  
                sub.append(1)  
            else:  
                sub.append(0)  

        if sum(sub[0:k-1]) == (k - 1):  
            res.append(maxi)  
        else:  
            res.append(-1)  
        n = len(nums)  

        for i in range(1,n - k + 1):     
            curr = max(nums[i:i + k])  
            if sum(sub[i:i + (k - 1)]) == (k - 1):  
                res.append(curr)  
            else:  
                res.append(-1)  
        return res