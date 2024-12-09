#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char board[3][3]; // Tic-Tac-Toe board

// Initialize the board
void initialize_board() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = '.'; // Empty cells
        }
    }
}

// Print the board for debugging
void print_board() {
    fprintf(stderr, "Current board state:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            fprintf(stderr, "%c ", board[i][j]);
        }
        fprintf(stderr, "\n");
    }
}

// Check for a winning or blocking move
bool find_winning_move(char player, int *move_row, int *move_col) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        // Check rows
        int count_player = 0, count_empty = 0, empty_col = -1;
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == player) count_player++;
            if (board[i][j] == '.') { count_empty++; empty_col = j; }
        }
        if (count_player == 2 && count_empty == 1) {
            *move_row = i;
            *move_col = empty_col;
            return true;
        }

        // Check columns
        count_player = 0; count_empty = 0; int empty_row = -1;
        for (int j = 0; j < 3; j++) {
            if (board[j][i] == player) count_player++;
            if (board[j][i] == '.') { count_empty++; empty_row = j; }
        }
        if (count_player == 2 && count_empty == 1) {
            *move_row = empty_row;
            *move_col = i;
            return true;
        }
    }

    // Check diagonals
    int diag1_player = 0, diag1_empty = 0, empty_diag1 = -1;
    int diag2_player = 0, diag2_empty = 0, empty_diag2 = -1;
    for (int i = 0; i < 3; i++) {
        if (board[i][i] == player) diag1_player++;
        if (board[i][i] == '.') { diag1_empty++; empty_diag1 = i; }

        if (board[i][2 - i] == player) diag2_player++;
        if (board[i][2 - i] == '.') { diag2_empty++; empty_diag2 = i; }
    }
    if (diag1_player == 2 && diag1_empty == 1) {
        *move_row = empty_diag1;
        *move_col = empty_diag1;
        return true;
    }
    if (diag2_player == 2 && diag2_empty == 1) {
        *move_row = empty_diag2;
        *move_col = 2 - empty_diag2;
        return true;
    }

    return false;
}

// Make a move (basic strategy)
void make_move(int valid_action_count, int valid_moves[][2], int *move_row, int *move_col) {
    // Try to win
    if (find_winning_move('X', move_row, move_col)) return;

    // Try to block the opponent
    if (find_winning_move('O', move_row, move_col)) return;

    // Otherwise, pick the first valid move
    *move_row = valid_moves[0][0];
    *move_col = valid_moves[0][1];
}

int main() {
    initialize_board(); // Set up the board

    // Game loop
    while (1) {
        int opponent_row, opponent_col;
        scanf("%d%d", &opponent_row, &opponent_col);

        // Update the board with the opponent's move
        if (opponent_row != -1 && opponent_col != -1) {
            board[opponent_row][opponent_col] = 'O';
        }

        int valid_action_count;
        scanf("%d", &valid_action_count);

        int valid_moves[valid_action_count][2];
        for (int i = 0; i < valid_action_count; i++) {
            scanf("%d%d", &valid_moves[i][0], &valid_moves[i][1]);
        }

        // Debugging: Print the board
        print_board();

        // Decide on a move
        int move_row = 0, move_col = 0;
        make_move(valid_action_count, valid_moves, &move_row, &move_col);

        // Update the board with our move
        board[move_row][move_col] = 'X';

        // Output the move
        printf("%d %d\n", move_row, move_col);
    }

    return 0;
}
