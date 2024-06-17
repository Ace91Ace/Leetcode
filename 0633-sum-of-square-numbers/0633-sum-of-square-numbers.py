class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))


        while right >= left:
            curr = right*right + left*left
            if curr == c:
                return True
            elif curr > c:
                right-=1
            else:
                left+=1
        return False