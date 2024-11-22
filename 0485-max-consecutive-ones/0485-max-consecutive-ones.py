class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc = c = 0

        for i in range(len(nums)):
            if nums[i] == 1 :
                print(i)
                c += 1
            else:
                c = 0
            maxc = max(maxc,c)
        return maxc
        