// A transformation sequence from word beginWord to word endWord using a
// dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
// such that:
//
//     Every adjacent pair of words differs by a single letter. Every si for 1
//     <= i <= k is in wordList. Note that beginWord does not need to be in
//     wordList. sk == endWord
//
// Given two words, beginWord and endWord, and a dictionary wordList, return all
// the shortest transformation sequences from beginWord to endWord, or an empty
// list if no such sequence exists. Each sequence should be returned as a list
// of the words [beginWord, s1, s2, ..., sk].

#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <climits>
#include <unordered_set>
using namespace std;
class Solution {
protected:
    bool isAble(const string &a, const string &b){
        if(a.size()!=b.size())
            return false;
        int c{};
        for(int i{}; i<b.size();i++){
            c+=(a[i]==b[i]);
        }
        return c==1;
    }
    void bfs(const vector<vector<int>> &g,vector<int> parent[],int n,int sr,int ds){
        vector <int> dist(n,1005);
        queue <int> q;
        q.push(sr);
        parent[sr]={-1};
        dist[sr]=0;
        while(!q.empty()){
            int x=q.front();
            q.pop();
            for(int u:g[x]){
                if(dist[u]>dist[x]+1){
                    dist[u]=dist[x]+1;
                    q.push(u);
                    parent[u].clear();
                    parent[u].push_back(x);
                }
                else if(dist[u]==dist[x]+1)
                    parent[u].push_back(x);
            }
        }
    }
    void shortestPaths(vector<vector<int>> &Paths, vector<int> &path, vector<int> parent[],int node){
        if(node==-1){
            Paths.push_back(path);
            return ;
        }
        for(auto u:parent[node]){
            path.push_back(u);
            shortestPaths(Paths,path,parent,u);
            path.pop_back();
        }
    }
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        int n=wordList.size(),sr=-1,ds=-1;
        vector<vector<string>> ANS;
        for(int i=0;i<n;i++){
            if(wordList[i]==beginWord)
                sr=i;
            if(wordList[i]==endWord)
                ds=i;
        }
        if(ds==-1)
            return ANS;
        if(sr==-1){
            wordList.emplace(wordList.begin(),beginWord);
            sr=0;
            ds++;
            n++;
        }
        vector <vector<int>> g(n,vector<int>()),Paths;
        vector <int> parent[n],path;
        for(int i=0;i<n-1;i++)
            for(int j=i+1;j<n;j++)
                if(isAble(wordList[i],wordList[j])){
                    g[i].push_back(j);
                    g[j].push_back(i);
                }
        bfs(g,parent,n,sr,ds); 
        shortestPaths(Paths,path,parent,ds);
        for(auto u:Paths){
            vector <string> now;
            for(int i=0;i<u.size()-1;i++)
                now.push_back(wordList[u[i]]);
            reverse(now.begin(),now.end());
            now.push_back(wordList[ds]);
            ANS.push_back(now);
        }
        return ANS;
    }
};
vector<vector<string>> findLadders(string beginWord, const string& endWord, vector<string>& wordList) {
    unordered_set<string> st (wordList.begin(),wordList.end());
    unordered_set<string> visited;
    vector<vector<string>> ans;
    queue<vector<string>> q;
    q.push({beginWord});
    while(!q.empty()){
        int size = q.size();
        while(size--){
            auto curr_path = q.front();
            q.pop();
            string last = curr_path.back();
            for(int i = 0 ; i < last.size() ; ++i){
                auto temp = last;
                for(char ch = 'a' ; ch <= 'z' ; ++ch){
                    temp[i] = ch;
                    if(st.find(temp) != st.end()){
                        auto new_path = curr_path;
                        new_path.push_back(temp);
                        visited.insert(temp);
                        if(temp == endWord)
                            ans.push_back(new_path);
                        else
                            q.push(new_path);
                    }
                }
            }
        }
        for(auto& str : visited)
                st.erase(str);
    }
    return ans;
}
