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
public:
    int height (TreeNode* root){

        if (root == nullptr){
            return 0;
        }

        int p1 = height(root -> left);
        int p2 = height(root -> right);
        
        return max(p1,p2) +1;
    }

    bool isBalanced(TreeNode* root) {
        
        if (root == nullptr){
            return true;
        }

        bool x1= isBalanced(root -> right);
        bool x2 = isBalanced(root -> left);
        bool x3 = abs(height(root -> right) - height(root -> left)) <= 1;

        if (x1 && x2 && x3){
            return true;
        }

        return 0;
    }
};