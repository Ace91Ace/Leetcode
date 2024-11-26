class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        tab = [0]*n
        c = 0
        w = -1

        for i,j in edges:
            tab[j] = -1
        
        for i in range(n):
            if tab[i] == 0:
                w = i
                c += 1
        
        return w if c == 1 else -1