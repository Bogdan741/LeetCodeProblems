// You are given an array of integers arr and an integer target.
//
// You have to find two non-overlapping sub-arrays of arr each with a sum equal
// target. There can be multiple answers so you have to find an answer where
// the sum of the lengths of the two sub-arrays is minimum.
//
// Return the minimum sum of the lengths of the two required sub-arrays, or
// return -1 if you cannot find such two sub-arrays.

#include <algorithm>
#include <limits>
#include <vector>
using namespace std;
class Solution {
public:
  int minSumOfLengths(vector<int> &arr, int target) {
    size_t n = arr.size();
    vector<int> prefix(n);
    vector<int> suffix(n);
    int i{}, j{}, sum{};
    int mini = numeric_limits<int>::max();
    while (j < n) {
      sum += arr[j];
      while (sum > target) {
        sum -= arr[i];
        ++i;
      }
      if (sum == target) {
        mini = min(mini, j - i + 1);
      }
      prefix[j] = mini;
      ++j;
    }
    i = n - 1, j = n - 1;
    mini = numeric_limits<int>::max();
    sum = 0;
    while (j >= 0) {
      sum += arr[j];
      while (sum > target) {
        sum -= arr[i];
        i--;
      }
      if (sum == target) {
        mini = min(mini, i - j + 1);
      }
      suffix[j] = mini;
      j--;
    }
    int ans = numeric_limits<int>::max();
    for (int k = 0; k < n - 1; k++) {
      ans = min(ans, suffix[k + 1] + prefix[k]);
    }
    if (ans == numeric_limits<int>::max())
      return -1;
    return ans;
  }
};
