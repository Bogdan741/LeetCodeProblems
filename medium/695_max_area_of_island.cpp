#include <vector>
#include <deque>
#include <utility>

using namespace std;
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;
        int n = grid.size();
        int m = grid[0].size();
        // Find the island and compare the areas
        for(int i{}; i < n; ++i){
            for(int j{}; j < m; ++j){
                if(grid[i][j] == 1){
                    int current_area=1;
                    deque<pair<int,int>> bfs;
                    bfs.push_back({i,j});
                    grid[i][j] = 0;
                    while(!bfs.empty()){
                        auto current = bfs.back();
                        bfs.pop_back();
                        if(current.first < n - 1 && grid[current.first+1][current.second] == 1){
                            ++current_area;
                            bfs.push_back({current.first+1, current.second});
                            grid[current.first+1][current.second] = 0;
                        }
                        if(current.first > 0 && grid[current.first-1][current.second] == 1){
                            ++current_area;
                            bfs.push_back({current.first-1, current.second});
                            grid[current.first-1][current.second] = 0;
                        }
                        if(current.second < m - 1 && grid[current.first][current.second+1] == 1){
                            ++current_area;
                            bfs.push_back({current.first, current.second+1});
                            grid[current.first][current.second+1] = 0;
                        }
                        if(current.second > 0 && grid[current.first][current.second-1] == 1){
                            ++current_area;
                            bfs.push_back({current.first, current.second-1});
                            grid[current.first][current.second-1] = 0;
                        }
                    }
                    max_area = max(max_area, current_area);
                }
            }
        }
        return max_area;
    }
};
