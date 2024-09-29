class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''index1 = 0
        index2 = 0
        for i in range(len(nums)):
            j=i+1
            while j!=len(nums):
                if nums[i]+nums[j]==target:
                    index1 = i
                    index2 = j
                j+=1
        return index1, index2'''

        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return num_map[complement], index
            num_map[num] = index