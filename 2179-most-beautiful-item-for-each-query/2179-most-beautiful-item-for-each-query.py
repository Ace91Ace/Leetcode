from typing import List  

class Solution:  
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:  
        items.sort(key=lambda x: x[1], reverse=True)  

        res = []  

        if not items:  
            return [0] * len(queries)  

        for query in queries:  
            found = False  
            for j in items:  
                if j[0] <= query:  
                    res.append(j[1])  
                    found = True  
                    break  
            
            if not found:  
                res.append(0)  

        return res