// Given an integer array nums, return the number of longest increasing
// subsequences.
//
// Notice that the sequence has to be strictly increasing.

#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        int res{};
        int max_len{};
        vector<pair<int,int>> dp(n,{1,1});
        for(int i = 0; i < n; ++i ){
            for(int j = 0; j < i; ++j){
                if(nums[i] > nums[j]){
                    if(dp[i].first == dp[j].first + 1) dp[i].second += dp[j].second;
                    if(dp[i].first < dp[j].first + 1) dp[i] = {dp[j].first + 1, dp[j].second};
                }
            }
            if(max_len == dp[i].first) res += dp[i].second;
            if(max_len < dp[i].first){
                max_len = dp[i].first;
                res = dp[i].second;
            }
        }
        return res;
    }
};
