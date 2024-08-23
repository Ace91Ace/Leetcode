class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        lon = 1
        seq = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] +1:
                seq+=1
            elif nums[i] != nums[i-1] :
                lon = max(seq,lon)
                seq = 1
        return max(lon,seq)

        
