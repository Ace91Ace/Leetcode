class Solution {  
public:  
    int height(TreeNode* root) {  
        if (root == nullptr) {  
            return 0;  
        }  
        return max(height(root->right), height(root->left)) + 1;  
    }  

    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {  
        vector<vector<int>> ans;  
        if (root == nullptr) return ans;  

        int n = height(root);  
        queue<TreeNode*> q;  
        q.push(root);  

        for (int i = 0; i < n; i++) {  
            int ls = q.size();  
            vector<int> ln(ls);  

            for (int j = 0; j < ls; j++) {  
                TreeNode* curr = q.front();  
                q.pop();  

                if (i % 2 == 0) {  
                    ln[j] = curr->val;  
                } else {  
                    ln[ls - 1 - j] = curr->val;  
                }  

                if (curr->left) {  
                    q.push(curr->left);  
                }  
                if (curr->right) {  
                    q.push(curr->right);  
                }  
            }  

            ans.push_back(ln);  
        }  

        return ans;  
    }  
};