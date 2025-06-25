class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if i == 0 else 1 for i in nums]
        sm, ml = 0, 0
        pref = {0:-1}

        for i,x in enumerate(nums):
            sm += x
            if sm in pref:
                ml = max(ml,i-pref[sm])
            else:
                pref[sm] = i
        return ml
            