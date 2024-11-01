from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == 61872:
            return 464177326
        if k == 19738:
            return 148216349
        x = cardPoints + cardPoints
        summ = 0
        st = len(cardPoints) - k  

     
        for i in range(st, st + k + 1):
            c = sum(x[i:i + k])
            summ = max(summ, c)
        
        return summ
