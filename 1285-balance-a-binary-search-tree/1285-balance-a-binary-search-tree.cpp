class Solution
{
private:
    vector<TreeNode *> arr;
    void inOrder(TreeNode *curr)
    {
        if (curr == nullptr)
            return;
        inOrder(curr->left);
        arr.push_back(curr);
        inOrder(curr->right);
    }

    TreeNode *solve(int left, int right)
    {
        if (left > right)
            return nullptr;
        int mid = (left + right) / 2;
        TreeNode *curr = arr[mid];
        curr->left = solve(left, mid - 1);
        curr->right = solve(mid + 1, right);
        return curr;
    }

public:
    TreeNode *balanceBST(TreeNode *root)
    {
        inOrder(root);
        return solve(0, arr.size() - 1);
    }
};