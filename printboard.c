void printboard(char board [3][3][3][3]);



void printboard(char board [3][3][3][3]){
	for (int i = 0; i < 3; i++){
		int j = 0;
		for (int k = 0; k < 3; k++){
			for (int l1 = 0; l < 3; l1++){
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
		}
		printf("\n");
	}

}
