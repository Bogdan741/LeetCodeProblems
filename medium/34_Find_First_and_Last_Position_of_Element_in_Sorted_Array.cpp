// Given an array of integers nums sorted in non-decreasing order, find the
// starting and ending position of a given target value.
//
// If target is not found in the array, return [-1, -1].
//
// You must write an algorithm with O(log n) runtime complexity.
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

// Solve the task.
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto first = lower_bound(nums.begin(), nums.end(), target);
        if(first == nums.end() || *first != target){
            return {-1,-1};
        }
        auto last = upper_bound(nums.begin(), nums.end(), target);

        int first_index = distance(nums.begin(), first );
        int last_index = distance(nums.begin(), last - 1);
        return {first_index, last_index};
    }
};

// Solution with custom implementation of 

int lower(const vector<int>&nums, int target){
    int left = 0;
    int right = nums.size();
    while (left < right){
        int mid = left + (right - left) / 2;
        if (nums[mid] >= target){
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
int upper(const vector<int>&nums, int target){
    int left = 0;
    int right = nums.size();
    while (left < right){
        int mid = left + (right - left) / 2;
        if (nums[mid] > target){
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
// def binary_search(array) -> int:
//     def condition(value) -> bool:
//         pass
//
//     left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
//     while left < right:
//         mid = left + (right - left) // 2
//         if condition(mid):
//             right = mid
//         else:
//             left = mid + 1
//     return left
int main(){
    vector<int> arr = {5,7,7,8,8,10};
    cout << lower(arr, 8);
    cout << upper(arr, 8);
}
