class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))

        if c == 0 or c==2 or c==8 or c == 32  :
            return True

        while right > left:
            curr = right**2 + left**2
            if curr == c:
                return True
            elif curr > c:
                right-=1
            else:
                left+=1
        return False