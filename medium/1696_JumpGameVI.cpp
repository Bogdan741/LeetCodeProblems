#include <vector>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;
class Solution {
public:
    // Too slow O(n*k)
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> memoized_array(n);
        memoized_array[n-1] = nums[n-1];
        for(int i{n-2}; i >= 0; --i){
            memoized_array[i] = nums[i] + *std::max_element(memoized_array.begin()+i+1, memoized_array.begin()+min(n,i+1+k));
        }
        return memoized_array[0];
    }

    // Improved version O(n) because amortized complixity for keeping deque in tack is O(1)
    // we add and remove maximum the n elements during the work
    int maxResultBetter(vector<int>& nums, int k) {
        int n = nums.size();
        deque<pair<int,int>> moves{{nums[n-1], n-1}};
        for(int i{n-2}; i >= 0; --i){
            int key = nums[i] + moves.front().first;
            while(!moves.empty() && moves.back().first < key){
                moves.pop_back();
            }
            moves.push_back({key, i});
            while(moves.front().second - i >= k){
                moves.pop_front();
            }
        }
        return moves.back().first;
    }
};

int main(){
    int n;
    int k;
    cin >> n >> k;
    vector<int> nums(n);
    std::istream_iterator<int> is{cin};
    copy_n(is, n, back_inserter(nums));
    cout << Solution().maxResultBetter(nums, k);
    return 0;
}
