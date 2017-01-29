void printboard(char board [3][3][3][3]);
void print(char c);


void printboard(char board [3][3][3][3]){
	for (int i = 0; i < 3; i++){
		int j = 0;
		for (int k = 0; k < 3; k++){
			for (int l1 = 0; l1 < 3; l1++){
				//printf("%c",board[i][j][k][l1]);
				print(board[i][j][k][l1]);
			}
			printf(" ");
			for (int l2 = 0; l2 < 3; l2++){
				//printf("%c",board[i][j+1][k][l2]);
				print(board[i][j+1][k][l2]);
			}
			printf(" ");
			for (int l3 = 0; l3 < 3; l3++){
				//printf("%c",board[i][j+2][k][l3]);
				print(board[i][j+2][k][l3]);
			}
			printf("\n");
		}
		printf("\n");
	}

}

// Auxilliary print method for easy visualization
void print(char c) {
	if (c == '0')
		printf("_");
	else if (c == '1')
		printf("X");
	else if (c == '2')
		printf("O");
}
