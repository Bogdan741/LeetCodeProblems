// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
//
// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#include <vector>
#include <utility>
using namespace std;
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for(int i = 0; i < n/2 + n%2 ; ++i){
            for(int j = 0; j < n/2; ++j){
                swap(matrix[n - 1 - j][i],  matrix[n - 1 - i][n - j - 1]);
                swap(matrix[n - 1 - i][n - j - 1], matrix[j][n - 1 -i]);
                swap(matrix[j][n - 1 - i], matrix[i][j]);
            }
        }
    }
};
