class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        vector<int> pre(n);
        pre[0] = arr[0];
        vector<int> ans(queries.size());

        for(int i=1; i<n; i++)
        {
            pre[i] = pre[i-1]^arr[i];
        }

        int k = 0;

        for(auto it: queries)
        {
            int i = it[0];
            int j = it[1];

            if(i==0)
            {
                ans[k] = pre[j];
            }
            else
            {
                ans[k] = pre[j]^pre[i-1];
            }

            k++;
        }

        return ans;
    }
};