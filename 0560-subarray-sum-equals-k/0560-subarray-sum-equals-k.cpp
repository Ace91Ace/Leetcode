class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        int n = nums.size();
        if (n==0){
            return 0;
        }
        int curr = 0;
        int res = 0;
        map[0] = 1;
        for (int i : nums){
            curr += i;
            if (map.find(curr - k)!= map.end()){
                res += map[curr-k];
            }
            map[curr]++;
        }
        return res;
    }
};