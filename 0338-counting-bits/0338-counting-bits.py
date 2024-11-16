class Solution:
    def countBits(self, n: int) -> List[int]:
        def bit(n):
            return bin(n)[2:].count('1')
        res =[]
        for i in range(n+1):
            res.append(bit(i))
        return res
