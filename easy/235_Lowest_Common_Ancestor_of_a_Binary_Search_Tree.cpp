// Given a binary search tree (BST), find the lowest common ancestor (LCA) node
// of two given nodes in the BST.
//
// According to the definition of LCA on Wikipedia: “The lowest common ancestor
// is defined between two nodes p and q as the lowest node in T that has both p
// and q as descendants (where we allow a node to be a descendant of itself).”


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode *firstPtr = root;
        TreeNode *secondPtr = root;
        TreeNode *parent = nullptr;
        while(firstPtr==secondPtr){
            parent = firstPtr;
            firstPtr = p->val < firstPtr->val ? firstPtr->left : p->val > firstPtr->val ? firstPtr->right : firstPtr;
            secondPtr = q->val < secondPtr->val ? secondPtr->left : q->val > secondPtr->val ? secondPtr->right : secondPtr;}
        return parent;
    }
};
