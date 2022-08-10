#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    static bool comp(vector<int> &a, vector<int> &b) {
        if(a[0] == b[0])
            return a[1] < b[1];
        return a[0] < b[0];
    }
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), Solution::comp);
        int  n = people.size();
        vector<vector<int>> ans(n, vector<int> (2,-1));
        for(vector<int> &v : people) {
            int i = 0, count = v[1];
            while(i < n) {
                if(ans[i][1] != -1 && ans[i][0] < v[0]) {
                    i++;
                }
                else if(ans[i][1] == -1 && count > 0) {
                    count--;
                    i++;
                }
                else if(ans[i][1] != -1 && ans[i][0] >= v[0]) {
                    count--;
                    i++;
                }
                else {
                    ans[i][0] = v[0];
                    ans[i][1] = v[1];
                    break;
                }
            }
        }
        return ans;
    }
};;
