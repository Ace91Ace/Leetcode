class Solution:
    def solve(self,nums,ans,ind):
        if ind>=len(nums):
            ans.append(nums[:])
            return
        
        for i in range(ind,len(nums)):
            nums[ind],nums[i] = nums[i],nums[ind]
            self.solve(nums,ans,ind+1)
            nums[ind],nums[i] = nums[i],nums[ind]


    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(digits) == 0:
            return ans
        self.solve(nums,ans,0)
        return ans