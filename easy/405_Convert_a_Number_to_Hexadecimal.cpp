// Given an integer num, return a string representing its hexadecimal
// representation. For negative integers, two’s complement method is used.
//
// All the letters in the answer string should be lowercase characters, and
// there should not be any leading zeros in the answer except for the zero
// itself.
//
// Note: You are not allowed to use any built-in library method to directly
// solve this problem.
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
class Solution {
public:
    string toHex(int num) {
        if(num == 0)
            return "0";
        unsigned res=num;
        
        string hexRes;
        int hexMask = 0xf;
        for(int i{}; i < sizeof(int)*2 && res; ++i){
            int hexDigit = res&hexMask;
            res = res>>4;
            if(hexDigit>9) hexRes+=hexDigit%10+97;
            else hexRes+=hexDigit+48;
        }
        return {hexRes.rbegin(), hexRes.rend()};
    }
};

int main(){
    cout << Solution().toHex(-26);
}

// switch(hexDigit){
//     case 0x0: hexRes += "0"; break;
//     case 0x1: hexRes += "1"; break;
//     case 0x2: hexRes += "2"; break;
//     case 0x3: hexRes += "3"; break;
//     case 0x4: hexRes += "4"; break;
//     case 0x5: hexRes += "5"; break;
//     case 0x6: hexRes += "6"; break;
//     case 0x7: hexRes += "7"; break;
//     case 0x8: hexRes += "8"; break;
//     case 0x9: hexRes += "9"; break;
//     case 0xa: hexRes += "a"; break;
//     case 0xb: hexRes += "b"; break;
//     case 0xc: hexRes += "c"; break;
//     case 0xd: hexRes += "d"; break;
//     case 0xe: hexRes += "e"; break;
//     case 0xf: hexRes += "f"; break;
// }
