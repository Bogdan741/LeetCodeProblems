// You are given a positive integer num consisting only of digits 6 and 9.
//
// Return the maximum number you can get by changing at most one digit (6
// becomes 9, and 9 becomes 6).
class Solution {
public:
    int maximum69Number (int num) {
        // Max num 10**4
        int power = 10*10*10;
        int tmp = num;
        for(int i=3; i >=0; --i){
            if(tmp / power == 6){
                return num+(9-6)*power;
            }
            tmp=tmp%power;
            power /= 10;
        }
        return num;
    }
};
