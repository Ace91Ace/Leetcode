class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        x = [i%2 for i in nums]
        pref = {0:1}
        sm, res = 0, 0
        for i in x:
            sm += i
            if sm-k in pref:
                res += pref[sm-k]
            if sm in pref:
                pref[sm] += 1
            else:
                pref[sm] = 1
        return res

            
        