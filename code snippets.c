

char boardWinner(char board[3][3][3][3], int checkRow, int checkCol){

	// vertical

	char subBoard[3][3] = board[checkRow][checkCol];
	if (subBoard[0][0] == subBoard[0][1] && subBoard[0][1] == subBoard[0][2])
		return subBoard[0][0];
	if (subBoard[1][0] == subBoard[1][1] && subBoard[1][1] == subBoard[1][2])
		return subBoard[1][0];
	if (subBoard[2][0] == subBoard[2][1] && subBoard[2][1] == subBoard[2][2])
		return subBoard[2][0];

	// horizontal
	if (subBoard[0][0] == subBoard[1][0] && subBoard[1][0] == subBoard[2][0])
		return subBoard[0][0];
	if (subBoard[0][1] == subBoard[1][1] && subBoard[1][1] == subBoard[2][1])
		return subBoard[0][1];
	if (subBoard[0][2] == subBoard[1][2] && subBoard[1][2] == subBoard[2][2])
		return subBoard[0][2];

	// diagonals
	if (subBoard[0][0] == subBoard[1][1] && subBoard[1][1] == subBoard[2][2])
		return subBoard[0][0];
	if (subBoard[2][0] == subBoard[1][1] && subBoard[1][1] == subBoard[0][2])
		return subBoard[2][0];

	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			if (subBoard[i][j] == 'E'){
				return 'E';
			}
		}
	}
	return 'F'
}




















