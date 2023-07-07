#include <climits>
#include <iostream>
#include <limits>
#include <map>
#include <utility>
#include <vector>
using namespace std;

// ### Trying to do DP approuch:
// When we iterate over the list of answers we can do the following operations
// - toggle boolean value
// - skip
// if we skip and the letter is not equal to the prev, we reset the couter and
// set prev to current letter (so we need to keep track of the last letter and
// couter) if choose to toggle we need to decrement k and set prev the selected
// letter So it seems dp will not be a case here cause theare not a subproblems
// and momoizing is not a case also.
//
// ### Sliding window:
// Lets find how many T and F in a row we can get:
//

class Solution {
public:
  int maxConsecutiveAnswers(string answerKey, int k) {
    int max_false = count_max_symbols_in_row(k, 'F', answerKey);
    int max_true = count_max_symbols_in_row(k, 'T', answerKey);
    return max(max_true, max_false);
  }

  int count_max_symbols_in_row(int toggle, char symbol, const string &seq) {
    int max_symbol = INT_MIN;
    int toggles_left = toggle;
    int start = 0;
    int n = seq.size();
    for (int i{0}; i < n; ++i) {
      while (toggles_left < 0) {
        if (seq[start++] != symbol) {
          toggles_left += 1;
        }
      }
      if (seq[i] != symbol) {
        toggles_left -= 1;
      }
      if (toggles_left >= 0) {
        max_symbol = max(max_symbol, i - start + 1);
      }
    }
    return max_symbol;
  }
};

// The same solution but with single path, since we can merge both loops into
// one
class Solution1 {
public:
  int maxConsecutiveAnswers(string keys, int k) {
    // support variables
    int i = 0, j = 0, len = keys.size(), res = 1, ts = 0, fs = 0;
    // parsing keys
    while (j < len) {
      // extending the window right
      if (keys[j++] == 'T')
        ts++;
      else
        fs++;
      // restricting the window left, if necessary
      while (min(ts, fs) > k) {
        if (keys[i++] == 'T')
          ts--;
        else
          fs--;
      }
      res = max(res, j - i);
    }
    return res;
  }
};
