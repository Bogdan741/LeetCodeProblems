// There is an m x n rectangular island that borders both the Pacific Ocean and
// Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
// and the Atlantic Ocean touches the island's right and bottom edges.
//
// The island is partitioned into a grid of square cells. You are given an m x
// n integer matrix heights where heights[r][c] represents the height above sea
// level of the cell at coordinate (r, c).
//
// The island receives a lot of rain, and the rain water can flow to
// neighboring cells directly north, south, east, and west if the neighboring
// cell's height is less than or equal to the current cell's height. Water can
// flow from any cell adjacent to an ocean into the ocean.
//
// Return a 2D list of grid coordinates result where result[i] = [ri, ci]
// denotes that rain water can flow from cell (ri, ci) to both the Pacific and
// Atlantic oceans.

#include <vector>
#include <queue>
#include <utility>
using namespace std;

class Solution {
private:
    static constexpr int dirs[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<bool>> p_visited(m,vector<bool>(n,false));
        vector<vector<bool>> a_visited(m,vector<bool>(n,false));
        for(int i=0; i < m; ++i){
            dfs(m,n,i,0,p_visited, heights);
            dfs(m,n,i,n-1,a_visited, heights);
        }
        for(int i=0; i < n; ++i){
            dfs(m,n,0,i,p_visited, heights);
            dfs(m,n,m-1,i,a_visited, heights);
        }
        
        vector<vector<int>> res;
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                if (p_visited[i][j] && a_visited[i][j]){
                    res.push_back({i,j});
                }
            }
        }
        return res;
    }
    void dfs(int m, int n, int i, int j, vector<vector<bool>> &visited, vector<vector<int>> matrix){
        queue<pair<int,int>> q;
        q.push({i,j});
        while(!q.empty()){
            pair<int,int> cur = q.front();
            visited[cur.first][cur.second] = true;
            q.pop();
            for(int k=0; k < 4; ++k){
                int x = cur.first + dirs[k][0];
                int y = cur.second + dirs[k][1];
                if(x < 0 || x >= m || y < 0 || y >= n || visited[x][y] || matrix[x][y] < matrix[cur.first][cur.second]){
                    continue;
                }
                q.push({x,y});
            }
        }
    }
};

