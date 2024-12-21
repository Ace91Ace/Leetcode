class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {

        vector<vector<int>>adj(n);
        for(auto edge:edges){
            int node1=edge[0];
            int node2=edge[1];
            adj[node1].push_back(node2);
            adj[node2].push_back(node1);
        }

        int cnt=0; 

        dfs(0,-1,adj,values,k,cnt);
        return cnt;
        
    }
    int dfs(int currnode,int parentnode,vector<vector<int>>& adj,vector<int>& values, int k,int& cnt){
        int sum=0; 

        for(auto neighbor:adj[currnode] ){
            if(neighbor !=parentnode){
                sum+=dfs(neighbor,currnode,adj,values,k, cnt);
                sum=sum%k;
            }

        }
        sum+=values[currnode];
        sum%=k;
        if(sum==0)cnt++;
        return sum;
    }
};