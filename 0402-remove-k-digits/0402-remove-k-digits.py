class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        num = [int(i) for i in num]
        for i in num:
            while stk and stk[-1] > i and k:
                stk.pop()
                k -= 1
            stk.append(i)
        
        while k and stk:
            stk.pop()
            k -= 1
        stk = [str(i) for i in stk]
        res = "".join(stk)
        res = res.lstrip('0')
        return "0" if res == "" else res
        