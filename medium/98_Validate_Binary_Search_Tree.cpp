// Given the root of a binary tree, determine if it is a valid binary search
// tree (BST).
//
// A valid BST is defined as follows:
//
//     The left subtree of a node contains only nodes with keys less than the
//     node's key. The right subtree of a node contains only nodes with keys
//     greater than the node's key. Both the left and right subtrees must also
//     be binary search trees.


// TAG: Binary Tree, DFS

#include <limits.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    bool helpFunction(TreeNode* root, long long lboundary, long long rboundary){
        if(!root)
            return true;
        else
            return root->val > lboundary && root->val < rboundary &&
            helpFunction(root->left, lboundary, root->val) &&
            helpFunction(root->right, root->val, rboundary);
    }
public:
    bool isValidBST(TreeNode* root) {
        return helpFunction(root,LLONG_MIN,LLONG_MAX);
    }
};
