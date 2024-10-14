class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        sum = 0
        for i in range(k):
            x = -heappop(heap)
            sum += x
            heappush(heap,-ceil(x/3))
        return sum