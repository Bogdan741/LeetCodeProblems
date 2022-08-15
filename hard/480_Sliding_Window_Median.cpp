// The median is the middle value in an ordered integer list. If the size of the
// list is even, there is no middle value. So the median is the mean of the two
// middle values.
//
//     For examples, if arr = [2,3,4], the median is 3. For examples, if arr =
//     [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
//
// You are given an integer array nums and an integer k. There is a sliding
// window of size k which is moving from the very left of the array to the very
// right. You can only see the k numbers in the window. Each time the sliding
// window moves right by one position.
//
// Return the median array for each window in the original array. Answers within
// 10-5 of the actual value will be accepted.
//

#include <set>
#include <vector>
using namespace std;
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window(nums.begin(), nums.begin() + k);
        auto mid = next(window.begin(), k / 2);
        vector<double> medians;
        medians.push_back((double(*mid) + *prev(mid, 1 - k%2))/2);
        for(int i{k};i < nums.size();++i){
            window.insert(nums[i]);
            if (nums[i] < *mid)
                mid--;
            if (nums[i - k] <= *mid)
                mid++;

            window.erase(window.lower_bound(nums[i - k]));
            medians.push_back((double(*mid) + *prev(mid, 1 - k%2))/2);
        }
        return medians;
    }
};
