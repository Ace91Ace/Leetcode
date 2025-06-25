class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = {0:1}
        res, sm = 0, 0

        for i in nums:
            sm += i
            if (sm-k) in pref:
                res += pref[(sm-k)]
            if sm in pref:
                pref[sm] += 1
            else:
                pref[sm] = 1
        return res