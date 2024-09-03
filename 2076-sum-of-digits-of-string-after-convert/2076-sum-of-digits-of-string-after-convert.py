class Solution:
    def getLucky(self, s: str, k: int) -> int:
        asc = ""

        for i in range(len(s)):
            asc += str(ord(s[i]) - 96)
        
        for i in range(k):
            sumx = 0
            for j in range(len(asc)):
                sumx += int(asc[j])
            asc = str(sumx)

        return int(asc)