class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = 0
        md = 1
        if (dividend < 0):
            md = -md
            dividend = abs(dividend)
        if (divisor < 0):
            md = -md
            divisor = abs(divisor)
        nn = 1
        dvd = dividend
        dvr = divisor
        sn = 0
        while (dvd >= dvr):
            nn = 1
            dd = dvr
            while (dvd >= dd):
                sn += nn
                dvd -= dd
                dd += dd
                nn += nn

        ans = sn

        if (md < 0):
            ans = -ans
        if (ans > 2 ** 31 - 1):
            ans = 2 ** 31 - 1
        if (ans < -2 ** 31):
            ans = -2 ** 31
        return (ans)