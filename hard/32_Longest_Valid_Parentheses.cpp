#include <string>
#include <stack>
#include <iostream>
using namespace std;
class Solution {
private:
    static constexpr char OPEN_BRACKET = '(';
    static constexpr char CLOSE_BRACKET = ')';
public:
    int longestValidParentheses(string s) {
        stack<int> stack;
        stack.push(-1);
        int maxlen{};
        int count{};
        for(int i{}; i < s.size(); ++i){
            if(s[i]==OPEN_BRACKET){
                stack.push(i);
            } else {
                stack.pop();
                if(stack.empty()){
                    stack.push(i);
                } else {
                    maxlen = max(maxlen, i - stack.top());
                }
            }
        }
        return maxlen;
    }
};

// Solution1 and Solution2 seem to use the same idea, but soultion1 i came out with 
class Solution1{
public:
    int longestValidParentheses(string s) {
        return max(longestValidParenthesesHelp(s, '('),
                   longestValidParenthesesHelp({s.rbegin(), s.rend()}, ')') );
    }
    int longestValidParenthesesHelp(string s, char bracket) {
        int stack{};
        int maxCount{};
        int count{};
        for(char ch: s){
            if (ch == bracket){
                stack++;
            } else {
                if(stack>0){
                    stack--;
                    count+=2;
                    if (stack == 0)
                        maxCount = max(count, maxCount);
                } else {
                    count = 0;
                }
            }
        }
        return maxCount;
    }
};

class Solution2{
public:
    int longestValidParenthesesHelp(string s, char par) {
        int left = 0, right = 0, maxlength = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxlength = max(maxlength, 2 * right);
            } else if (right >= left) {
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == ')') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxlength = max(maxlength, 2 * right);
            } else if (right >= left) {
                left = right = 0;
            }
        }
        return maxlength;
    }
};

int main(){
    string s = "(((())()(((()))";
    cout << min(Solution().longestValidParentheses(s), Solution().longestValidParentheses({s.rbegin(), s.rend()}));
    return 0;
}
