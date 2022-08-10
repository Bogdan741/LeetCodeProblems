#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        const auto first = std::find(nums.begin(), nums.end(), target);
        if (first == nums.end()){
            return {-1,-1};
        }
        const auto second = std::find(nums.rbegin(), nums.rend(), target);
        return {(int)distance(nums.begin(), first), (int)distance(second, nums.rend())};
    }
};
