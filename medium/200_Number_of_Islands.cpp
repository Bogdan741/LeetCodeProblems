// Given an m x n 2D binary grid grid which represents a map of '1's (land) and
// '0's (water), return the number of islands.
//
// An island is surrounded by water and is formed by connecting adjacent lands
// horizontally or vertically. You may assume all four edges of the grid are
// all surrounded by water.


#include <vector>
#include <deque>
#include <utility>

using namespace std;
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        int n = grid.size();
        int m = grid[0].size();
        // Find the island and compare the areas
        for(int i{}; i < n; ++i){
            for(int j{}; j < m; ++j){
                if(grid[i][j] == '1'){
                    deque<pair<int,int>> bfs;
                    bfs.push_back({i,j});
                    grid[i][j] = '0';
                    while(!bfs.empty()){
                        auto current = bfs.front();
                        bfs.pop_front();
                        if(current.first < n - 1 && grid[current.first+1][current.second] == '1'){
                            bfs.push_back({current.first+1, current.second});
                            grid[current.first+1][current.second] = '0';
                        }
                        if(current.first > 0 && grid[current.first-1][current.second] == '1'){
                            bfs.push_back({current.first-1, current.second});
                            grid[current.first-1][current.second] = '0';
                        }
                        if(current.second < m - 1 && grid[current.first][current.second+1] == '1'){
                            bfs.push_back({current.first, current.second+1});
                            grid[current.first][current.second+1] = '0';
                        }
                        if(current.second > 0 && grid[current.first][current.second-1] == '1'){
                            bfs.push_back({current.first, current.second-1});
                            grid[current.first][current.second-1] = '0';
                        }
                    }
                    ++count;
                }
            }
        }
        return count;
    }
};
