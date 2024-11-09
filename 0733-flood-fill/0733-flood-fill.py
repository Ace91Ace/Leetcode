class Solution:  
    def bfs(self, adj, node, col):  
        r = len(adj)  
        c = len(adj[0])  
        
        q = deque([node])  
        vis = [[False] * c for _ in range(r)]  
        original_color = adj[node[0]][node[1]]  
        
        if original_color == col:  
            return adj  
        
        adj[node[0]][node[1]] = col  

        dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        while q:  
            rt, ct = q.popleft()  

            for dr, dc in dire:  
                nr, nc = rt + dr, ct + dc  
                if 0 <= nr < r and 0 <= nc < c and adj[nr][nc] == original_color and not vis[nr][nc]:  
                    vis[nr][nc] = True  
                    adj[nr][nc] = col  
                    q.append((nr, nc))  
        
        return adj  

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:  
        start = (sr, sc)  
        return self.bfs(image, start, color)