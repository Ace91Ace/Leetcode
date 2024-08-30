class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> maxi;

        for (int i = 0; i < k; i++) {
            maxi.push(nums[i]);
        }

        int n = nums.size();

        for (int i = k ;i<n ;i++){
            if(maxi.top()<nums[i]){
                maxi.pop();
                maxi.push(nums[i]);
            }
        }
        return maxi.top();
    }
};