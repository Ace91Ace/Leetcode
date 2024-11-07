class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [(bin(candidates[i])[2:]) for i in range(len(candidates))]
        x = len(max(bits,key = len))
        for i in range(len(bits)):
            bits[i] = ((x - len(bits[i]))*'0')+bits[i]
        
        maxn = 0
        for i in range(x):
            count = 0
            for j in bits:
                if j[i] == '1':
                    count+=1
            maxn = max(maxn,count)

        return maxn