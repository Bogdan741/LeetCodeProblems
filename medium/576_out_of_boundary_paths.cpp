#include <vector>
#include <iostream>
using namespace std;

constexpr long long operator "" _b(unsigned long long l) {
    return l * 1000 * 1000 * 1000;
}

class Solution {
private:
    using value_type = unsigned long long;
    vector<vector<vector<value_type>>> memoize_table;
    int _m;
    int _n;
    int _maxMove;
public:
    int findPaths(int n, int m, int maxMove, int startRow, int startColumn) {
        _m = m;
        _n = n;
        this->memoize_table = vector<vector<vector<value_type>>>(n, vector<vector<value_type>>(m, vector<value_type>(maxMove+1, -1)));
        return f(startRow, startColumn, maxMove);
    }
private:
    value_type f(int i, int j, int k){
        if(k == 0) return 0;

        value_type key = memoize_table[i][j][k];

        if(key == -1){
            value_type paths{0};
            // Check for bounderyes
            if(i == 0) ++paths; 
            if(i == (_n - 1)) ++paths; 

            if(j == 0) ++paths; 
            if( j == (_m - 1)) ++paths; 

            if(i > 0) paths += f(i-1, j, k-1);
            if(i < _n - 1) paths += f(i+1, j, k-1);
            if(j > 0) paths += f(i, j-1, k-1);
            if(j < _m - 1) paths+= f(i, j+1, k -1);

            memoize_table[i][j][k] = paths % (1_b + 7);
            return paths;
        }
        return key;
    }
};

int main(){
    int m, n, maxMove, startRow, startColumn;
    cin >> m >> n >> maxMove >> startRow >> startColumn;
    cout << Solution().findPaths(m, n, maxMove, startRow, startColumn);
    return 0;
}
