#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include "printboard.c"

char opposite(char currColour);
char boardChecker(char board[3][3][3][3], int checkRow, int checkCol);
int algorithm(char board[3][3][3][3], int playRow, int playCol, char currColour, char us);
<<<<<<< HEAD
int getScore(char board[3][3][3][3], int checkRow, int checkCol, char currColour);
void printboard(char baord[3][3][3][3]);


void printboard(char board [3][3][3][3]){
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



=======
int getScore(char board[3][3][3][3], int checkRow, int checkCol, char currColour, char us);
>>>>>>> d533bcbbc8cd5c4872aae3f13630eb43e4711cbf

// Checks to see what the subboard state is
// Returns '1' or '2' if X or O wins
// Returns '0' if there is still an empty space in the subboard
// Returns 'F' if the board is full
char boardChecker(char board[3][3][3][3], int checkRow, int checkCol){

	// the 3x3 subboard
  //char subBoard[][] = board[checkRow][checkCol];
  //char** subBoard = board[checkRow][checkCol];

  printf("Row %d Col %d\n", checkRow, checkCol);
  // vertical
	if (board[checkRow][checkCol][0][0] == board[checkRow][checkCol][0][1] && board[checkRow][checkCol][0][1] == board[checkRow][checkCol][0][2])
		return board[checkRow][checkCol][0][0];
	if (board[checkRow][checkCol][1][0] == board[checkRow][checkCol][1][1] && board[checkRow][checkCol][1][1] == board[checkRow][checkCol][1][2])
		return board[checkRow][checkCol][1][0];
	if (board[checkRow][checkCol][2][0] == board[checkRow][checkCol][2][1] && board[checkRow][checkCol][2][1] == board[checkRow][checkCol][2][2])
		return board[checkRow][checkCol][2][0];

	// horizontal
	if (board[checkRow][checkCol][0][0] == board[checkRow][checkCol][1][0] && board[checkRow][checkCol][1][0] == board[checkRow][checkCol][2][0])
		return board[checkRow][checkCol][0][0];
	if (board[checkRow][checkCol][0][1] == board[checkRow][checkCol][1][1] && board[checkRow][checkCol][1][1] == board[checkRow][checkCol][2][1])
		return board[checkRow][checkCol][0][1];
	if (board[checkRow][checkCol][0][2] == board[checkRow][checkCol][1][2] && board[checkRow][checkCol][1][2] == board[checkRow][checkCol][2][2])
		return board[checkRow][checkCol][0][2];

	// diagonals
	if (board[checkRow][checkCol][0][0] == board[checkRow][checkCol][1][1] && board[checkRow][checkCol][1][1] == board[checkRow][checkCol][2][2])
		return board[checkRow][checkCol][0][0];
	if (board[checkRow][checkCol][2][0] == board[checkRow][checkCol][1][1] && board[checkRow][checkCol][1][1] == board[checkRow][checkCol][0][2])
		return board[checkRow][checkCol][2][0];

	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			if (board[checkRow][checkCol][i][j] == '0'){
				return '0';
			}
		}
	}
  // board is full
	return 'F';
}


/**
* Algorithm that returns a score for a particular subBoard
*
* playRow and playCol mirror the valid indices for the moves in a particular subboard
* ie: char subboard[][] = board[playRow][playCol] corresponds to board[][][playRow][playCol]
*/
int algorithm(char board[3][3][3][3], int playRow, int playCol, char currColour, char us) {

  //char[][] subBoard = char[playRow][playCol];
  //int points[3][3];
  char boardCheckResult = boardChecker(board, playRow, playCol);
  printf("Board check is %c\n", boardCheckResult);
  if (boardCheckResult == '0'){
    return getScore(board, playRow, playCol, currColour, us);
  }

  // We would have to make a bad move, by sending the opponent to a full or won section
  if (currColour == us) {
    return -1000;

  // the opponent would make a bad move by sending us to a full or won section
  } else {
    return 1000;
  }
}

// Returns a score for the subboard given by checkRow and checkCol

// 2 cases to consider:
// 1) The character to consider is 'us' ---> increase score
// 2) The character to consider is the enemy ---> decrease score
// The rationale is that we want to go to places where we have lots of ours
// We want to send the enemy to places with lots of ours
// Return value is positive if lots of us
int getScore(char board[3][3][3][3], int checkRow, int checkCol, char currColour, char us) {
  // char[k][l]
  //char subBoard[3][3] = board[checkRow][checkCol];

  int pointTotal = 0;
  for (int k2 = 0; k2 < 3; k2++) {
    for (int l2 = 0; l2 < 3; l2++) {

      char curr = board[checkRow][checkCol][k2][l2];

      if (curr == us) {
        if (k2 == 1 && l2 == 1)
          pointTotal += 5;
        else if ((k2+l2) % 2 == 0)
          pointTotal += 3;
        else
          pointTotal += 1;
      } else if (curr == opposite(us)) {
        if (k2 == 1 && l2 == 1)
          pointTotal -= 5;
        else if ((k2+l2) % 2 == 0)
          pointTotal -= 3;
        else
          pointTotal -= 1;
      }

      printf("%c  %d\n", curr, pointTotal);
    }
  }

  return pointTotal;
}

// Returns the opposite player
// 'X' is 1, 'O' is 2
char opposite(char currColour) {
  if (currColour == '1')
    return '2';
  return '1';
}

<<<<<<< HEAD
int main(int arc, char** argv) {
	double time = atof(argv[1]);
	char us = argv[2][0];
	int move = argv[2][1] - '0';
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
	printboard(board);
    printf("Hello world");
    return 0;
=======
int main(int argc, char** argv) {

	double time = atof(argv[1]); 	//gets time given in seconds
	char us = argv[2][0];			//tells us who we are playing as (either X or O)
	int move = argv[2][1] - '0';	//tells us where we are allowed to move
  //printf("We are %c\nPlay in board %d\n\n", us, move);
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
  printboard(board);
  printf("\n%d", algorithm(board, 2, 2, '1', '2'));
  return 0;
>>>>>>> d533bcbbc8cd5c4872aae3f13630eb43e4711cbf
}
