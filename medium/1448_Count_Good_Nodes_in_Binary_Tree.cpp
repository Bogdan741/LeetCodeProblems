#include<climits>
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
    int _counter=0;
    void helpFunction(TreeNode *root, int max_value){
        if (root==nullptr) return;
        if( root->val >= max_value ){
            max_value = root->val;
            ++_counter;
        }
        helpFunction(root->left, max_value);
        helpFunction(root->right, max_value);
    }
public:
    int goodNodes(TreeNode* root) {
        helpFunction(root, INT_MIN);
        return _counter;
    }
    
};
