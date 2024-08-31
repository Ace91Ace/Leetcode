class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[len(nums)-k%len(nums):] + nums[0:len(nums)-k%len(nums)]
        