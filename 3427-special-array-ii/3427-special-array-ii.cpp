class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        
        vector<vector<int>> c;
        
        for(int i=0;i<nums.size()-1;i++){
            if((nums[i]+nums[i+1])%2==0){
                
                c.push_back({i, i+1});
            }
        }
        
        int n=queries.size();
        
        vector<bool> res(n);
        
        for(int i=0;i<n;i++){
            int l=0, r=c.size()-1;
            
            bool flag=true;
            if(queries[i][0]==queries[i][1]){
                res[i]=true;
                continue;
            }
            while(l<=r){
                
                int mid=l+((r-l)>>1);
                
                if((c[mid][0]>=queries[i][0] and c[mid][0]<queries[i][1]) or (c[mid][1]>queries[i][0] and c[mid][1]<=queries[i][1])){
                    flag=false;
                    break;
                    
                }
                
                else if(c[mid][1]<=queries[i][0])
                    l=mid+1;
                else
                    r=mid-1;
            }
            
            res[i]=flag;
            
            
        }
        
        return res;
        
        
        
    }
};