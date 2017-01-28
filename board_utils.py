import sys

# this will check if the entire 9x9 board is full.
def board_is_full(board):
	for sub_board in board:
		for row in sub_board:
			for char in row:
				if char == '':
					return False

	return True



# this will check if a sub board is playable.
# returns characters
# will return the color that the board is owned by,
# if tied in that board, it will return 'E'
# if board is full it will return 'F'
def sub_board_is_full(board, play_row, play_col):
	sub_board = board[play_row][play_col]
	# vertical
	if (sub_board[0][0] == sub_board[0][1] and sub_board[0][1] == sub_board[0][2]):
		return sub_board[0][0];
	if (sub_board[1][0] == sub_board[1][1] and sub_board[1][1] == sub_board[1][2]):
		return sub_board[1][0];
	if (sub_board[2][0] == sub_board[2][1] and sub_board[2][1] == sub_board[2][2]):
		return sub_board[2][0];

	# horizontal
	if (sub_board[0][0] == sub_board[1][0] and sub_board[1][0] == sub_board[2][0]):
		return sub_board[0][0];
	if (sub_board[0][1] == sub_board[1][1] and sub_board[1][1] == sub_board[2][1]):
		return sub_board[0][1];
	if (sub_board[0][2] == sub_board[1][2] and sub_board[1][2] == sub_board[2][2]):
		return sub_board[0][2];

	# diagonals
	if (sub_board[0][0] == sub_board[1][1] and sub_board[1][1] == sub_board[2][2]):
		return sub_board[0][0];
	if (sub_board[2][0] == sub_board[1][1] and sub_board[1][1] == sub_board[0][2]):
		return sub_board[2][0];

	for row in sub_board:
		for char in row:
			if char == 'E':
				return char

	return 'F'
board = [[[[0 for x in range(3)] for y in range(3)] for z in range(3)] for k in range(3)]
def printboard(board):
	j = 0
	for i in range(3):
		for k in range(3):
			for l1 in range(3):
				sys.stdout.write(str(board[i][j][k][l1]) + ' ')
			sys.stdout.write("  ")
			for l2 in range(3):
				sys.stdout.write(str(board[i][j+1][k][l2]) + ' ')
			sys.stdout.write("  ")
			for l3 in range(3):
				sys.stdout.write(str(board[i][j+2][k][l3]) + ' ')

			print ""

		print ""


printboard(board)


