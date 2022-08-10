#import <string>
#import <vector>
#import <algorithm>
using namespace std;

class Solution {
public:
    int numMatchingSubseq(string s, vector<string> &words) {
        vector<vector<int>> charMap(26);
        int n = s.size();
        for(int i{}; i < n; ++i ){
            charMap[s[i] - 'a'].push_back(i);
        }

        int res = words.size();
        for(auto& word: words){
            int last = -1;
            for(char ch: word){
                auto& cIndexes = charMap[ch - 'a'];
                auto it = upper_bound(cIndexes.begin(), cIndexes.end(), last);
                if(it == cIndexes.end()){
                    --res;
                    break;
                }
                else{
                    last = *it;
                }
            }
        }
        return res;
    }
};
