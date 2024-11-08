class Solution:
    def dfs(self,node, adjacency_list, visited):  
        visited[node] = 1   
        for neighbor in adjacency_list[node]:  
            if visited[neighbor] == 0:  
                self.dfs(neighbor, adjacency_list, visited)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = {}
        for i in range(len(isConnected)):
            adj[i] = []
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i!=j:
                    adj[i].append(j)
        vis = [0]*len(adj)
        count = 0

        for i in range(len(adj)):
            if vis[i]!=1:
                count += 1
                self.dfs(i,adj,vis)
        return count
    