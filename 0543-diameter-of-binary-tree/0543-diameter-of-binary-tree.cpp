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
    int height(TreeNode * root){
        
        if (root == nullptr){
            return 0;
        }
        
        int l = height(root->left);
        int r = height(root->right);
        
        return max(l,r) + 1;
        
    }
    
    
    int diameterOfBinaryTree(TreeNode* root) {

        if (root == nullptr){
            return 0;
        }
        
        int o1 = diameterOfBinaryTree(root -> left);
        int o2 = diameterOfBinaryTree(root -> right);
        int o3 = height(root->right) + height(root -> left) ;

        return max(o1, max(o2,o3)) ;
            
    }
};