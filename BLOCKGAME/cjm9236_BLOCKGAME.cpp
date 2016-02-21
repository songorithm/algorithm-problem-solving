// BLOCKGAME problem
// Author: JeongminCha (cjm9236@me.com)

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

std::vector<int> strategy;
char cache[1 << 25] = {-1, };        // 2^25-size
const int L_block[4][3][2] = {
	{{0,0},{1,0},{1,1}},
	{{0,0},{0,1},{1,1}},
	{{0,0},{0,1},{-1,1}},
	{{0,0},{1,0},{0,1}},
};
const int I_block[2][2][2] = {
    {{0,0},{1,0}},
    {{0,0},{0,1}},
};

int make_board(char input[5][5]) {
    int idx_board = 0;
    for (int row = 0; row < 5; row++) {
        for (int col = 0; col < 5; col++) {
            idx_board *= 2;
            if (input[row][col] == '#') {
                idx_board += 1;
            }
        }
    }
    return idx_board;
}

int index(int x, int y) {
    return 1 << (x + y*5);
}

bool empty(int& idx_board, int x, int y) {
    return (x >= 0 && x < 5) &&
            (y >= 0 && y < 5) && 
            (idx_board & index(x,y)) == 0;
}

bool L_available(int& idx_board, int row, int col, int shape) {
    // Check the block can be put in the specified location.
    for (int i = 0; i < 3; i++) {
        int y = row + L_block[shape][i][0];
        int x = col + L_block[shape][i][1];
        if (!empty(idx_board, x, y)) {
            return false;
        }
    }
    // Add the block (by OR operation)
    for (int i = 0; i < 3; i++) {
        int y = row + L_block[shape][i][0];
        int x = col + L_block[shape][i][1];
        idx_board |= index(x,y);
    }
    return true;
}

bool I_available(int& idx_board, int row, int col, int shape) {
    // Check the block can be put in the specified location.
    for (int i = 0; i < 2; i++) {
        int y = row + I_block[shape][i][0];
        int x = col + I_block[shape][i][1];
        if (!empty(idx_board, x, y)) {
            return false;
        }
    }
    // Add the block (by OR operation)
    for (int i = 0; i < 2; i++) {
        int y = row + I_block[shape][i][0];
        int x = col + I_block[shape][i][1];
        idx_board |= index(x,y);
    }
    return true;
}

void L_pop(int& idx_board, int row, int col, int shape) {
    // Delete the block (by XOR operation)
    for (int i = 0; i < 3; i++) {
        int y = row + L_block[shape][i][0];
        int x = col + L_block[shape][i][1];
        idx_board ^= index(x,y);
    }
}

void I_pop(int& idx_board, int row, int col, int shape) {
    // Delete the block (by XOR operation)
    for (int i = 0; i < 2; i++) {
        int y = row + I_block[shape][i][0];
        int x = col + I_block[shape][i][1];
        idx_board ^= index(x,y);
    }
}

void construct_all_strategies() {
    for (int row = 0; row < 5; row++) {
        for (int col = 0; col < 5; col++) {
            int idx_board = 0;
            // processing L-shaped block
            for (int shape = 0; shape < 4; shape++) {
                if (L_available(idx_board, row, col, shape)) {
                    strategy.push_back(idx_board);
                    L_pop(idx_board, row, col, shape);
                }
            }
            // processing I-shaped block
            for (int shape = 0; shape < 2; shape++) {
                if (I_available(idx_board, row, col, shape)) {
                    strategy.push_back(idx_board);
                    I_pop(idx_board, row, col, shape);
                }
            }
        }
    }
}

// Returns True if there's a way to win in the current board condition.
char check_winning_way(int idx_board) {
    char& ret = cache[idx_board];
    if (ret != -1) {
        return ret;
    }
    ret = 0;
    // For every strategies about putting new block
    for (int i = 0; i < strategy.size(); i++) {
        int new_block = strategy[i];
        // 1. new block is not overlapped with the existing blocks.
        // 2. failing is guranteed after the next new block is added.
        if ((new_block & idx_board) == 0 &&
            !check_winning_way(new_block | idx_board)) {
            ret = 1;
            break;
        }
    }
    return ret;
}

int main() {
    construct_all_strategies();
    int test_case = 0;
    std::cin >> test_case;
    while (test_case --) {
        char input[5][5];
    	memset(cache, -1, sizeof(cache));
        for (int i = 0; i < 5; i++) {
        	std::cin >> input[i];
        }
        int idx_board = make_board(input);
        bool result = check_winning_way(idx_board);
        if (result > 0) {
        	std::cout << "WINNING" << std::endl;
        } else {
        	std::cout << "LOSING" << std::endl;
        }
    }
    return 0;
}