class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hp = []
        for i in range(len(nums)):
            heapq.heappush(hp,[nums[i],i])
        
        for _ in range(k):
            x = heapq.heappop(hp)
            x[0] = x[0]*multiplier
            heapq,heappush(hp,x)
        
        hp = list(hp)
        hp.sort(key = lambda item: item[1])
        
        res = [i[0] for i in hp]
        
        return res
