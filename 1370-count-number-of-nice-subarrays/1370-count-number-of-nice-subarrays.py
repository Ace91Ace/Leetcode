class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        x = [i%2 for i in nums]
        pref = {0:1}
        sm, res = 0, 0

        for i in x:
            sm += i
            res += pref.get(sm-k, 0)
            pref[sm] = pref.get(sm, 0)+1
        return res
        

            
        