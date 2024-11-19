class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxs = 0
        count = defaultdict(int)
        curr = 0

        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            count[nums[r]] += 1

            if r - l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                curr -= nums[l]
                l += 1
            
            if len(count) == r - l + 1 == k:
                maxs = max(maxs,curr)
        
        return maxs

        