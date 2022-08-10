// Given an array of integers nums and an integer target, return indices of the
// two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may
// not use the same element twice.
//
// You can return the answer in any order.

#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        //Key is the number and value is its index in the vector.
        unordered_map<int, int> hash;
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++) {
            int numberToFind = target - numbers[i];

                //if numberToFind is found in map, return them
            if (hash.find(numberToFind) != hash.end()) {
                        //+1 because indices are NOT zero based
                result.push_back(hash[numberToFind] + 1);
                result.push_back(i + 1);			
                return result;
            }

                //number was not found. Put it in the map.
            hash[numbers[i]] = i;
        }
        return result;
    }
};

    // vector<int> twoSum(vector<int>& nums, int target) {
    //     vector<pair<int,int>> originalIndexes;
    //     for(int i{}; i< nums.size(); ++i){
    //         originalIndexes.push_back({nums[i],i});
    //     }
    //     sort(originalIndexes.begin(), originalIndexes.end());
    //     for(const auto & val: originalIndexes){
    //         auto it = lower_bound(originalIndexes.begin(), originalIndexes.end(), pair<int,int>{target - val.first, 0},
    //                               [](const pair<int,int>& a, const pair<int,int>& b){return a.first == b.first;});
    //         if (val.first + it->first == target) return {val.second, it->second};
    //     }
    //     return {};
    // }
