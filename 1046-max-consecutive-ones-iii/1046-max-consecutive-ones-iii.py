class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = nz = 0
        maxc = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                nz += 1

            while nz > k:
                if nums[l] == 0:
                    nz -= 1
                l += 1
            
            maxc = max(maxc,r-l + 1)
        
        return maxc
        