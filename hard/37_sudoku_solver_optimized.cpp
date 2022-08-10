#include <vector>
#include <algorithm>
#include <string>
using namespace std;
class Solution {
public:
    const static int BoardSize = 9;
    // const static int BoardHeight = 9;
    const static char EmptyCell = '.';
    void solveSudoku(vector<vector<char>>& board) {
        _board = board;
        solveUtil(0);
        board = _board;
    }
    bool solveUtil(int cell){
        if(cell >= BoardSize * BoardSize) return true;

        int i = cell / BoardSize; 
        int j = cell % BoardSize;
        for(int c{cell}; c < BoardSize*BoardSize; ++c){
            i = c / BoardSize; 
            j = c % BoardSize;
            if(_board[i][j] == EmptyCell){
                break;
            }
        }
        if(_board[i][j] != EmptyCell) return true;

        for(int k{}; k < BoardSize + 1; ++k){
            if(goodPath(i,j, k +'0')){
                _board[i][j] = k + '0'; // because ascii )
                if (solveUtil(i*BoardSize + j + 1)){
                    return true;
                }
            }
        }
        _board[i][j] = EmptyCell;
        return false;
    }
    bool goodPath(int row, int col, int digit) const{
        for (int i = 0; i < 9; i++) {
            if (_board[i][col] - '0' == digit)
                return false;

            if (_board[row][i] - '0' == digit)
                return false;

            if (_board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] - '0' == digit)
                return false;
            }
        return true;
    }
private:
    vector<vector<char>> _board;
};
