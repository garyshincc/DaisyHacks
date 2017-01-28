#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>


char opposite(char currColour);
char boardWinner(char board[3][3][3][3], int checkRow, int checkCol);
int algorithm(char board[3][3][3][3], int playRow, int playCol, char currColour, char us);
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




char boardWinner(char board[3][3][3][3], int checkRow, int checkCol){

	// the 3x3 subboard
  //char subBoard[][] = board[checkRow][checkCol];
  //char** subBoard = board[checkRow][checkCol];

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
			if (board[checkRow][checkCol][i][j] == 'E'){
				return 'E';
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
  if (boardWinner(board, playRow, playCol) == 'E'){
    return getScore(board, playRow, playCol, currColour);
  }

  // We would have to make a bad move, by sending the opponent to a full or won section
  if (currColour == us) {
    return -1000;

  // the opponent would make a bad move by sending us to a full or won section
  } else {
    return 1000;
  }


  // for (int k = 0; k < 3; k++) {
  //   for (int l = 0; l < 3; l++) {
  //     char currChar_PlayBoard = subBoard[k][l];
  //
  //     if (currChar_PlayBoard == 'E') {
  //
  //       // If someone has not won at the board then check the board's score
  //       if (boardWinner(board, k, l) == 'E') {
  //         points[k][l] = getScore(board, k, l)
  //       } else {
  //         // DO NOT want to play at a full or won board
  //         points[k][l]-= 1000;
  //       }
  //     }
  //   }
  // }

  // if (us == currColour) {
  //   return max(points);
  // } else {
  //   return min(points);
  // }
}


int getScore(char board[3][3][3][3], int checkRow, int checkCol, char currColour) {
  // char[k][l]
  //char subBoard[3][3] = board[checkRow][checkCol];

  int pointTotal = 0;
  for (int k2 = 0; k2 < 3; k2++) {
    for (int l2 = 0; l2 < 3; l2++) {

      char curr = board[checkRow][checkCol][k2][l2];

      if (curr == currColour) {
        if (k2 == 1 && l2 == 1)
          pointTotal += 5;
        else if ((k2+l2) % 2 == 0)
          pointTotal += 3;
        else
          pointTotal += 1;
      } else if (curr == opposite(currColour)) {
        if (k2 == 1 && l2 == 1)
          pointTotal -= 5;
        else if ((k2+l2) % 2 == 0)
          pointTotal -= 3;
        else
          pointTotal -= 1;
      }
    }
  }

  return pointTotal;
}

char opposite(char currColour) {
  if (currColour == 'X')
    return 'O';
  return 'X';
}

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
}
