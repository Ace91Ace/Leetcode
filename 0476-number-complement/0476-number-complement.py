class Solution:
    def findComplement(self, num: int) -> int:
        x = num.bit_length()
        mask = (1<<x)-1
        return mask^num