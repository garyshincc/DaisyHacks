#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void printboard(double time, char us, int move, char board [3][3][3][3]);
minimax(int level, double time_left, char us, int move);



minimax(int level, double time_left, char us, char turn, int move, char board[3][3][3][3]){
	if (level == 0){
		int col = move % 3;
		int row = move / 3;
		return algorithm(board, row, col, turn, us);
	}
	else if (terminal(board)){
		return tie_count_wins(us ,board);
	}
	get_moves(turn, board);
	if (turn == us){
		double best_val = -1000000;
		bool moves[9] = get_moves( turn, move, board);
		for (int i = 0; i )
	}
	else{
		double best_val = 1000000;
		bool moves[9] = get_moves( turn, move, board);
	}
}

void printboard(double time, char us, int move, char board [3][3][3][3]){
        printf("time: %lf\n", time);
        printf("us: %c\n", us);
        printf("move: %i\n", move);

        for (int i = 0; i < 3; i++){
                int j = 0;
                for (int k = 0; k < 3; k++){
                        for (int l1 = 0; l1 < 3; l1++){
                                printf("%c",board[i][j][k][l1]);
                        }
                        printf(" ");
                        for (int l2 = 0; l2 < 3; l2++){
                                printf("%c",board[i][j+1][k][l2]);
                        }
                        printf(" ");
                        for (int l3 = 0; l3 < 3; l3++){
                                printf("%c",board[i][j+2][k][l3]);
                        }
                        printf("\n");
                }
                printf("\n");
        }

}



int main(int argc, char ** argv){

	double time = atof(argv[1]); 	//gets time given in seconds
	char us = argv[2][0];			//tells us who we are playing as (either X or O)
	int move = argv[2][1] - '0';	//tells us where we are allowed to move

	char * raw_input_board = &argv[2][2];
	char board[3][3][3][3];
	for (int i = 0; i < 3; i++){
	for (int j = 0; j < 3; j++){
	for (int k = 0; k < 3; k++){
	for (int l = 0; l < 3; l++){
		board[i][j][k][l] = raw_input_board[27*i + 9*j + 3*k + l];
	}
	}
	}
	}
	


}