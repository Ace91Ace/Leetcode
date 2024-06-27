class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x = edges[0][0]
        
        for i in edges:
            if x not in i:
                return edges[0][1]
        return x
