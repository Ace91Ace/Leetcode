
class Solution:  
    def canSortArray(self, nums: List[int]) -> bool:  
        bits = [num.bit_count() for num in nums]
        n = len(nums)

        for i in range(n):
            for j in range(0,n-i-1):
                if bits[j] == bits[j+1]:
                    if nums[j] > nums[j + 1]:  
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]  
                        bits[j],bits[j+1] = bits[j+1],bits[j]
        return nums == sorted(nums)
        
        
        
        
       