#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        int left = 0;
        int right = n-1;
        while(1){
            int pos = _partition(nums, left, right);
            if (pos == k){
                return nums[k];
            }
            else if(pos > k){
                right = pos - 1;
            }
            else {
                left = pos + 1;
            }
        }

    }
    int _partition(vector<int> &nums, int left, int right){
        int i = left - 1;
        for(int j = left; j < right; ++j){
            if(nums[j] >= nums[right]){
                swap(nums[j], nums[++i]);
            }
        }
        swap(nums[++i], nums[right]);
        return i;
    }
};
