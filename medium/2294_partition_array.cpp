// You are given an integer array nums and an integer k. You may partition nums
// into one or more subsequences such that each element in nums appears in
// exactly one of the subsequences.
//
// Return the minimum number of subsequences needed such that the difference
// between the maximum and minimum values in each subsequence is at most k.
//
// A subsequence is a sequence that can be derived from another sequence by
// deleting some or no elements without changing the order of the remaining
// elements.

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int count=nums.size();
        int maxIdx = nums.size() - 1;
        int curIdx = nums.size() - 2;
        while(curIdx >= 0){
            if(nums[maxIdx]-nums[curIdx]>k){
                maxIdx = curIdx;
            }
            else{
                --count;
            }
            --curIdx;
        }
        return count;
    }
};
