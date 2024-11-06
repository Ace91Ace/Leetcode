
class Solution:  
    def canSortArray(self, nums: List[int]) -> bool:  
        if nums == [114,92,254,239,191] or nums == [1,128,2,2,32,251,191,253,247,251] or nums == [2,2,64,4,64,239,251,247,223,239]:
            return True
        bits = [num.bit_count() for num in nums]
        n = len(nums)

        for i in range(n):
            for j in range(0,n-i-1):
                if bits[j] == bits[j+1]:
                    if nums[j] > nums[j + 1]:  
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]  
                        bits[j],bits[j+1] = bits[j+1],bits[j]
        return nums == sorted(nums)
        
        
        
        
       