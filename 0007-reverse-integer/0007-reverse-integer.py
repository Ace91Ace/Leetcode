class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: neg = 1 
        else: neg = 0
        l = 1
        curr = abs(x)

        while curr // 10 > 0:
            l += 1
            curr = curr // 10
        res = 0
        x = abs(x)
        for _ in range(l):
            n = x % 10
            x = x // 10

            res = res + n * (10**(l-1))
            l -= 1


        if res >= 0 and res < 2**31:
            if neg:
                return -res
            return res
        return 0

