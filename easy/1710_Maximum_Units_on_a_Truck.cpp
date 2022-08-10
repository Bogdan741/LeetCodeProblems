/* You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]: */
/**/
/* numberOfBoxesi is the number of boxes of type i. */
/* numberOfUnitsPerBoxi is the number of units in each box of the type i. */
/* You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize. */
/**/
/* Return the maximum total number of units that can be put on the truck. */
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](vector<int> & a, vector<int> &b){
                      return !(a[1] < b[1]);
                  } 
                  );
        long long sum{};
        int count{};
        for(int i{0}; i < boxTypes.size(); i++){
            long long nBoxes = min(truckSize - count, boxTypes[i][0]);
            sum += nBoxes * boxTypes[i][1]; 
            count += nBoxes;
        }
        return sum;
    }
};
