// You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
// You can either start from the step with index 0, or the step with index 1.
// Return the minimum cost to reach the top of the floor.

#include <vector>
using namespace std;
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int next{cost[n-2]};
        int nextnext{cost[n-1]};
        
        for(int i{n-3}; i>=0; --i){
            int tmp = next;
            next = cost[i] + min(next, nextnext);
            nextnext = tmp;
        }
        return min(next, nextnext);
    }
};
