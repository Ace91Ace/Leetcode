from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        
        total_sum = sum(cardPoints)
        window_size = n - k
        min_subarray_sum = sum(cardPoints[:window_size])
        current_sum = min_subarray_sum

        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_subarray_sum = min(min_subarray_sum, current_sum)
        
        return total_sum - min_subarray_sum
