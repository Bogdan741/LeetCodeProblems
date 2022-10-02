
struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode() : val(0), left(nullptr), right(nullptr) {}
   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <iostream>
#include <queue>
#include <vector>
using namespace std;
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        if (!root)
            return {};
        vector<double> res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int count = 0;
            double total = 0;
            queue<TreeNode*> level_queue;
            while(!q.empty()){
                TreeNode* node = q.front();
                q.pop();
                ++count;
                total += node->val;
                if(node->left)
                    level_queue.push(node->left);
                if(node->right)
                    level_queue.push(node->right);
            }
            res.push_back(total / count);
            q = level_queue;
        }
        return res;
    }
};
