class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums[:] = [0]*nums.count(0)+[1]*nums.count(1)+[2]*nums.count(2)
        