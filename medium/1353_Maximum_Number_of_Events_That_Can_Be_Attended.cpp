// You are given an array of events where events[i] = [startDayi, endDayi].
// Every event i starts at startDayi and ends at endDayi.
//
// You can attend an event i at any day d where startTimei <= d <= endTimei.
// You can only attend one event at any time d.
//
// Return the maximum number of events you can attend.

#include <vector>
#include <algorithm>
#include <set>
using namespace std;
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end(), [](const vector<int> &e1, const vector<int> &e2){
                 return e1[0]==e2[0]? e1[1] < e2[1]:e1[0]<e2[0];
             });
        int end{};
        int count{};
        multiset<int> active;
        for(int i{}, d{};; ++d){
            while(!active.empty() && *(active.begin()) < d){
                active.erase(active.begin());
            }
            while(i < events.size() && events[i][0] == d){
                active.insert(events[i][1]);
                i++;
            }
            if(active.size() > 0) {
                ++count;
                active.erase(active.begin());
            }
            if(i >= events.size() && active.empty())
                break;
        }
        return count;
    }
};
