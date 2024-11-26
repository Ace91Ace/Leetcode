from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if edges == []:
            return 0 if n == 1 else -1

        x = set()
        y = set()

        for i in edges:
            x.add(i[0])
            y.add(i[1])
        
        w = list(x.difference(y))
        
        if len(w) != 1:
            return -1
        
        candidate = w[0]
        
        reachable = set()
        stack = [candidate]
        
        while stack:
            node = stack.pop()
            if node not in reachable:
                reachable.add(node)
                for edge in edges:
                    if edge[0] == node and edge[1] not in reachable:
                        stack.append(edge[1])
        
        if len(reachable) == n:
            return candidate
        
        return -1