#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        size_t r{matrix.size()},c{matrix[0].size()};
        vector<vector<int>> prefix(r+1,vector<int>(c, 0));
        prefix[r-1][c-1] = matrix[r-1][c-1];
        prefix[r][c-1] = 0;
        for(int i = c-2; i >= 0; --i){
            prefix[r-1][i] = prefix[r-1][i+1] + matrix[r-1][i];
            prefix[r][i] = 0;
        }
        for(int i = r-2; i >= 0; --i){
            prefix[i][c-1]=prefix[i+1][c-1] + matrix[i][c-1];
        }
        for(int i = r - 2; i>=0 ; --i){
            for(int j = c - 2; j>=0; --j){
                prefix[i][j] = prefix[i+1][j] + prefix[i][j+1] - prefix[i+1][j+1] + matrix[i][j];
            }
        }
        size_t count{0};
        for(int i{0}; i < r; ++i){
            for(int j{i+1}; j <= r; ++j){
                map<int,int> mp;
                mp[0] = 1;
                for(int k = c-1; k >= 0; --k){
                    int sum = prefix[i][k] - prefix[j][k];
                    int reqSum = sum - target;
                    count += mp[reqSum];
                    mp[sum]++;
                }
            }
        }
        return count;
    }
};
