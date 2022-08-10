#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>
#include <iterator>

using namespace std;
class Solution {
public:
    // Too slow O(n!)
    bool makesquare(vector<int>& matchsticks) {
        int sum = accumulate(matchsticks.begin(), matchsticks.end(), 0);
        int square[4] = {0};
        if(sum % 4 == 0){
            return helpFunction(matchsticks, square, 0, sum / 4);
        }
        return false;
    }
private:
    bool helpFunction(vector<int> &matchsticks, int square[4], int squareIndex, const int value){
        if(squareIndex == 4) return true;
        for(int i{0}; i < matchsticks.size(); ++i){
            if(square[squareIndex] + matchsticks[i] > value || matchsticks[i] == 0 ){
                continue;
            }
            int temp = matchsticks[i];
            square[squareIndex] += matchsticks[i];
            matchsticks[i] = 0;
            int squareIndexTmp = squareIndex;
            if(square[squareIndex] + matchsticks[i] == value ){
                ++squareIndexTmp;
            }
            if(helpFunction(matchsticks, square, squareIndexTmp, value)){ return true; }
            matchsticks[i] = temp;
            square[squareIndex] -= matchsticks[i];
        }
        return false;
    }
};

int main(){
    int n;
    cin >> n;
    vector<int> matchsticks;
    copy_n(istream_iterator<int>(cin), n, back_inserter(matchsticks));
    return Solution().makesquare(matchsticks);
}
