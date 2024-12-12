class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapify(gifts)

        for _ in range(k):
            x = floor(sqrt(-heapq.heappop(gifts)))
            heappush(gifts, -x)
        
        return -sum(gifts)

