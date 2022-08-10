// Write a program to solve a Sudoku puzzle by filling the empty cells.
//
// A sudoku solution must satisfy all of the following rules:
//
// Each of the digits 1-9 must occur exactly once in each row. Each of the
// digits 1-9 must occur exactly once in each column. Each of the digits 1-9
// must occur exactly once in each of the 9 3x3 sub-boxes of the grid. The '.'
// character indicates empty cells.
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

        for(int k{1}; k < BoardSize + 1; ++k){
            _board[i][j] = k + '0'; // because ascii )
            if(goodPath(i,j) && solveUtil(i*BoardSize + j + 1)){
                return true;
            }
        }
        _board[i][j] = EmptyCell;
        return false;
    }
    bool goodPath(int row, int col) const{
        return checkRow(row) && checkCol(col) && checkSmallSquare(row, col);
    }
    bool checkRow(int row) const{
        int mask[BoardSize]{0};
        for(int col{}; col < BoardSize; ++col){
            if(_board[row][col] == EmptyCell){
                continue;
            }
            mask[_board[row][col] - '1']++;
        }
        return find_if(begin(mask), end(mask), [](int count){return count > 1;}) == end(mask);
    }
    bool checkCol(int col) const{
        int mask[BoardSize]{0};
        for(int row{}; row < BoardSize; ++row){
            if(_board[row][col] == EmptyCell){
                continue;
            }
            mask[_board[row][col] - '1']++;
        }
        return find_if(begin(mask), end(mask), [](int count){return count > 1;}) == end(mask);
    }
    bool checkSmallSquare(int row, int col) const{
        int mask[BoardSize]{0};
        int rowS = row / 3;
        int colS = col / 3;
        for (int i{}; i < 3; ++i){
            for(int j{}; j < 3; ++j){
                if(_board[rowS*3 + i][colS*3 + j] == EmptyCell){
                    continue;
                }
                mask[_board[rowS*3 + i][colS*3 + j] - '1'] ++;
            }
        }
        return find_if(begin(mask), end(mask), [](int count){return count > 1;}) == end(mask);
    }
private:
    vector<vector<char>> _board;
};
int main(){
    vector<vector<char>> board = {{'5','3','.','.','7','.','.','.','.'},
                                {'6','.','.','1','9','5','.','.','.'},
                                {'.','9','8','.','.','.','.','6','.'},
                                {'8','.','.','.','6','.','.','.','3'},
                                {'4','.','.','8','.','3','.','.','1'},
                                {'7','.','.','.','2','.','.','.','6'},
                                {'.','6','.','.','.','.','2','8','.'},
                                {'.','.','.','4','1','9','.','.','5'},
                                {'.','.','.','.','8','.','.','7','9'}};
    Solution().solveSudoku(board);
}

