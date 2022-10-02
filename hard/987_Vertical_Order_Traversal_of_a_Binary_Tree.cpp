// Given the root of a binary tree, calculate the vertical order traversal of
// the binary tree.
//
// For each node at position (row, col), its left and right children will be at
// positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root
// of the tree is at (0, 0).
//
// The vertical order traversal of a binary tree is a list of top-to-bottom
// orderings for each column index starting from the leftmost column and ending
// on the rightmost column. There may be multiple nodes in the same row and
// same column. In such a case, sort these nodes by their values.
//
// Return the vertical order traversal of the binary tree.


// Solution: we traverse tree using multiset where (x) is the key of the structure (y and val) as value.
// Left leaf is y+1, x-1, right leaf y+1, x+1

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
class Solution {
    public:
        vector<vector<int>> verticalTraversal(TreeNode* root) 
        {
            map<int, multiset<pair<int, int>>> mp; // [x][y, val]
            traverse(root, 0, 0, mp);
            vector<vector<int>> res;
            for(auto& [x, st] : mp)
            {
                res.push_back({});
                for(auto& [y, val] : st) res.back().push_back(val);
            }
            return res;
        }
        
    protected:
        void traverse(TreeNode* node, int x, int y,  map<int, multiset<pair<int, int>>>& mp)
        {
            if(!node) return;
            mp[x].insert({y, node->val});
            traverse(node->left, x-1, y+1, mp);
            traverse(node->right, x+1, y+1, mp);
        }
};
