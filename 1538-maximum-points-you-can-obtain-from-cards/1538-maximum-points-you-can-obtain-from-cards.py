class Solution:  
    def maxScore(self, cardPoints: List[int], k: int) -> int:  
        n = len(cardPoints)  
        if k == n:  
            return sum(cardPoints)  
        
        summ = sum(cardPoints[-k:])  
        max_score = summ  

        for i in range(k):  
            summ = summ - cardPoints[-(k - i)] + cardPoints[i]  
            max_score = max(max_score, summ)  
        
        return max_score