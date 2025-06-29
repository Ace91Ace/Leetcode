class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sm, res = 0, 0
        pref = {0:1}

        for i in nums:
            sm += i
            if (sm - goal) in pref:
                res += pref[(sm-goal)]
            pref[sm] = pref.get(sm, 0)+1
        return res