class Solution:
    def maxTotalReward(self, nums: List[int]) -> int:
        reached = 1 << 0
        for v in sorted(set(nums)):
            reached |= (reached & ((1 << v) - 1)) << v
        return reached.bit_length() - 1