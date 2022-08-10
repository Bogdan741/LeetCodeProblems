#include <vector>
#include <deque>
#include <utility>
#include <string.h>
#include <queue>
#include <limits.h>

using namespace std;
class Solution {
private:
    using value = pair<int,pair<int,int>>;
    bool vis[201][201];
    int n,m;
    bool isValid(int i, int j){
        return !(i<0 || i>=m || j<0 || j>=n || vis[i][j]==true);
    }
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        vector<vector<int>> dir {{1,0},{-1,0},{0,1},{0,-1}};
            m = heightMap.size();
            if(m==0)
                return 0;
            n = heightMap[0].size();
            memset(vis,false,sizeof(vis));
            priority_queue<value, vector<value>, greater<value>> pq;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(i==0 || j==0 || i==m-1 || j==n-1){
                        pq.push({heightMap[i][j],{i,j}});
                        vis[i][j]=true;
                    }   
                }
            }
        int water = 0;
        int cur_height = INT_MIN;
        while(!pq.empty()){
            value pr =  pq.top();
            pq.pop();
            int height = pr.first;
            int i = pr.second.first;
            int j = pr.second.second;
            cur_height = max(cur_height,height);
            for(int d=0;d<4;d++){
                int x = i + dir[d][0];
                int y = j + dir[d][1];
                if(isValid(x,y)){
                   water += max(0, cur_height - heightMap[x][y]);
                   vis[x][y]=true;
                   pq.push({heightMap[x][y],{x,y}});
                }
            }            
        }
        return water;
    }

};
