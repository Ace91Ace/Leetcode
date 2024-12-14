from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_window = SortedList()  
        start = 0
        total_subarrays = 0
        
        for end in range(n):
            sorted_window.add(nums[end])
            
            while sorted_window[-1] - sorted_window[0] > 2:
                sorted_window.remove(nums[start])
                start += 1
            
            total_subarrays += end - start + 1
        
        return total_subarrays