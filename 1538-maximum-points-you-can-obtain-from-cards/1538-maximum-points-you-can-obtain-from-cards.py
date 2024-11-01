class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        # Initial score using the first k cards
        current_score = sum(cardPoints[:k])
        max_score = current_score
        
        # Use a sliding window to calculate the score by taking cards from the end
        for i in range(1, k + 1):
            current_score += cardPoints[-i] - cardPoints[k - i]
            max_score = max(max_score, current_score)
        
        return max_score