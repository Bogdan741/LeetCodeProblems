#include <string>
#include <cstdlib>
using namespace std;

class Solution {
public:
    string removeDigit(string number, char digit) {
        string mx = "";
        for(int i = 0; i < number.size(); i++){
            if(number[i]==digit){
                string s = number;
                s.erase(i, 1);
                mx = max(mx, s);
            }
        }
        return mx;
    }
};
