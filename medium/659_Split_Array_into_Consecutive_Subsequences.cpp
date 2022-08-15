// You are given an integer array nums that is sorted in non-decreasing order.
//
// Determine if it is possible to split nums into one or more subsequences such
// that both of the following conditions are true:
//
//     Each subsequence is a consecutive increasing sequence (i.e. each integer
//     is exactly one more than the previous integer). All subsequences
//     have a length of 3 or more.
//
// Return true if you can split nums according to the above conditions, or false
// otherwise.
//
// A subsequence of an array is a new array that is formed from the original
// array by deleting some (can be none) of the elements without disturbing the
// relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence
// of [1,2,3,4,5] while [1,3,2] is not).

#include <iostream>
#include <queue>
#include <vector>
#include <utility>
#include <unordered_map>
using namespace std;
// ------------------------------------------------------------------------
class Solution {
public:
     bool isPossible(const vector<int>& A) {
        unordered_map<int, int> left, end;
        for (int i: A) {
            left[i]++;
        }
        for (int i: A) {
            if (left[i] == 0) continue;
            left[i]--;
            if (end[i - 1] > 0) {   
                end[i - 1]--;
                end[i]++;
            } else if (left[i + 1] > 0 && left[i + 2] > 0) {
                left[i + 1]--;
                left[i + 2]--;
                end[i + 2]++;
            } else {   
                return false;
            }
        }
        return true;
    }
};
// ------------------------------------------------------------------------
int main(){
    std::cout << Solution().isPossible({1,2,3,4,4,5,5,6});
    return 0;
}
