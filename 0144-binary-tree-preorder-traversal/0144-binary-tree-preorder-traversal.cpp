/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    void pot (TreeNode* root, vector<int> &res){
        if(root){
            res.push_back(root->val);
            pot(root->left,res);
            pot(root->right,res);
        }
    }
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        pot(root,res);
        return res;
    }
};