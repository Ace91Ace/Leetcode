class Solution:
    def kthSmallestProduct(self, n1: List[int], n2: List[int], k: int) -> int:
        # Solution 1:
        def cnt(x):
            c = 0
            for a in n1:
                if a > 0:
                    c += bisect_right(n2, x // a)
                elif a < 0:
                    t = x // a + (1 if x % a else 0)
                    c += m2 - bisect_left(n2, t)
                else:
                    if x >= 0:
                        c += m2
            return c

        if len(n1) > len(n2):
            n1, n2 = n2, n1
        m2 = len(n2)
        lo = min(n1[0]*n2[0], n1[0]*n2[-1], n1[-1]*n2[0], n1[-1]*n2[-1])
        hi = max(n1[0]*n2[0], n1[0]*n2[-1], n1[-1]*n2[0], n1[-1]*n2[-1])
        while lo < hi:
            mid = (lo + hi) // 2
            if cnt(mid) >= k:   hi = mid
            else:               lo = mid + 1
        return lo