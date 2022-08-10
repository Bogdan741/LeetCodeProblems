#include <vector>
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
private:
    vector<int> _nums;
    TreeNode* createChild(int low, int high){
        if (low > high)
            return nullptr;
        int mid = low + (high - low) /2;
        TreeNode* parent = new TreeNode(_nums[mid]);
        parent->left = createChild(low, mid);
        parent->right = createChild(mid+1, high);
        return parent;

    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        _nums = nums;
        return createChild(0,nums.size() - 1);
    }
};
