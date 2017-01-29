


// getting valid moves
// input is double time, char us, int move, char board

#include <stdbool.h>

// since we cant return array types in C, and struct will complicate things,
// pass in a pointer to an array, and it will be modified here
void get_valid_moves(char board[3][3][3][3], int playRow, int playCol, bool * valid_moves[9]);

/*
when calling, use
bool valid_moves[9];
bool* valid_moves = &valid_moves;

*/

void get_valid_moves(char board[3][3][3][3], int playRow, int playCol, bool * valid_moves[9]){
	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			if (board[playRow][playCol][i][j] == 'E'){
				valid_moves[i+j] = true;
			}
			else{
				valid_moves[i+j] = false;
			}
		}
	}
}
