#include<set>
#include<vector>
// TODO read about ext module
#include<ext/pb_ds/assoc_container.hpp>
using namespace std;
class Solution {
public:

    // Actually for python such solutions works pretty fine with 99%
    // But for cpp it is TLE -_-(due to distance take linear time, other
    // implementation of multiset should actually work)
    // with assoc_container implementation it actually pass ok
    vector<int> countSmallerTest(vector<int>& nums) {
        multiset<int> sl(nums.begin(), nums.end());
        vector<int> res;
        for(int el: nums){
            auto idx = sl.lower_bound(el);
            const auto pos = std::distance(sl.begin(), idx);
            res.push_back(pos);
            sl.erase(idx);
        }
        return res;
    }
    vector<int> countSmaller(vector<int>& nums) {
        multiset<int> sl;
        for(auto it=nums.rbegin(); it != nums.rend(); ++it){
            const auto idx = sl.lower_bound(*it);
            auto pos = std::distance(sl.begin(), idx);
            *it = pos;
            sl.insert(*it);
        }
        return nums;
    }
};
