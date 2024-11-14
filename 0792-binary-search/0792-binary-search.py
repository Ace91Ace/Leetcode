class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        h = len(nums) - 1 
        
        
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else :
                h = mid - 1
        return -1