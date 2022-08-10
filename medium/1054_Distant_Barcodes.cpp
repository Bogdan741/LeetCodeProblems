// In a warehouse, there is a row of barcodes, where the ith barcode is
// barcodes[i].
//
// Rearrange the barcodes so that no two adjacent barcodes are equal. You may
// return any answer, and it is guaranteed an answer exists.
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;
class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        map<int,int> counting;
        for(int barcode: barcodes) ++counting[barcode];
        priority_queue<pair<int,int>> common;
        for(const auto & [k,v]: counting){
            common.push({v,k});
        }
        vector<int> res;
        while(!common.empty()){
            bool fs{false};
            auto firstcommon = common.top();
            common.pop();
            if(common.empty()){
                res.push_back(firstcommon.second);
                break;
            }
            auto secondcommon = common.top();
            common.pop();
            res.push_back(firstcommon.second);
            res.push_back(secondcommon.second);
            if( --firstcommon.first > 0) common.push(firstcommon); 
            if( --secondcommon.first > 0) common.push(secondcommon); // never passes if previous doesn't pass
        }
        return res;
    }
};
