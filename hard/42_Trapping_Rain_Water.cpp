#include <vector>
using namespace std;
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int left{}, right{n - 1};
        int left_max{}, right_max{};
        int res{};
        while(left <= right){
            int l = height[left];
            int r = height[right];
            if(l <= r){
                if(l > left_max){
                    left_max = l;
                } else {
                    res += left_max - l;
                }
                ++left;
            } else {
                if(r > right_max){
                    right_max = l;
                } else {
                    res += right_max - r;
                }
                ++right;
            }
        }
        return res;
    }
};
