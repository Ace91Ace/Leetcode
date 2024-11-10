class Solution:
    def minimumSubarrayLength(self, nums, k):
        cnt = [0] * 30
        cur = 0
        res = float('inf')
        j = 0
        
        for i in range(len(nums)):
            for b in range(30):
                if (1 << b) & nums[i]:
                    if cnt[b] == 0:
                        cur += (1 << b)
                    cnt[b] += 1
            
            while cur >= k and j <= i:
                res = min(res, i - j + 1)
                for b in range(30):
                    if (1 << b) & nums[j]:
                        cnt[b] -= 1
                        if cnt[b] == 0:
                            cur -= (1 << b)
                j += 1
        
        return res if res != float('inf') else -1