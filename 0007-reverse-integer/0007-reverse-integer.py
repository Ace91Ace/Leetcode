class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        neg = 0
        if x[0] == '-': 
            neg = 1
            x = x[1:]
        x = int(x[::-1])

        if x >= 0 and x < 2**31:
            if neg:
                return -x
            return x
        return 0

