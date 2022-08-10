//
// Given an integer array nums, return the length of the longest strictly
// increasing subsequence.
//
// A subsequence is a sequence that can be derived from an array by deleting
// some or no elements without changing the order of the remaining elements.
// For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
//

#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> tail; 
        for(int num: nums){
            if (tail.empty() || num > tail.back()){
                tail.push_back(num);
            } else {
                int index = lower_bound(tail.begin(), tail.end(), num) - tail.begin();
                tail[index] = num;
            }
        }
        return tail.size();
    }
};
