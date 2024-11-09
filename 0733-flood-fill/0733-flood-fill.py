class Solution:
    def bfs(self,adj,node, col):
        r = len(adj)
        c = len(adj[0])

        q = deque([node])
        vis = [[False]*c for _ in range(r)]
        vis[node[0]][node[1]] = True
        if adj[node[0]][node[1]] != 0:
            adj[node[0]][node[1]] = col

        dire = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            rt,ct = q.popleft()
            if adj[rt][ct] != 0:
                adj[r][c] = col


            for dr ,dc in dire:
                nr,nc = rt + dr, ct + dc
                if 0 <= nr < r and 0<= nc < c and adj[nr][nc] == 1 and not vis[nr,nc]:
                    vis[nr][nc] = True
                    q.append((nr,nc))
        return bfsres

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = (sr,sc)
        x = self.bfs(image,start,color)
        return x
