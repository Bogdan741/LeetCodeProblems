struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

using namespace std;
class Solution {
public:
    void flatten(TreeNode* root) {
        if(root == nullptr){
            return;
        }
        flattenToRight(root);
    }
    TreeNode* flattenToRight(TreeNode* root){
        if(!root->left && !root->right){
            return root;
        }
        if(!root->left){
            return flattenToRight(root->right);
        }
        if(!root->right){
            TreeNode* endL = flattenToRight(root->left);
            root->right = root->left;
            root->left = nullptr;
            return endL;
        }
        TreeNode* endL = flattenToRight(root->left);
        TreeNode* endR = flattenToRight(root->right);
        endL->right = root->right;
        root->right = root->left;
        root->left = nullptr;
        return endR;
    }
};
