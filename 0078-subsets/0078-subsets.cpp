class Solution {
private:
    void subs(int i, vector<vector<int>> &ans ,vector<int> out, vector<int> nums){
        if (i >= nums.size()){
            ans.push_back(out);
            return;
        }

        subs(i+1,ans,out,nums);

        out.push_back(nums[i]);
        subs(i+1,ans,out,nums);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> out;
        int i = 0;
        subs(i,ans,out,nums);
        return ans;
    }
};