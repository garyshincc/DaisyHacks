import sys

# this will check if the entire 9x9 board is full.
def board_is_full(board):
	for sub_row in board:
		for sub_board in sub_row:
			for row in sub_board:
				for char in row:
					if char == '0':
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
			if char == '0':
				return char

	return 'F'


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

# returns a 2-D array of valid moves
# the array will be 3 by 3 size type int
# play row and play col correspond to which sub_board
# is to be played currently.


# test board
def get_valid_moves(board, play_row, play_col):

	valid_moves = [[1 for x in range(3)] for y in range(3)]
	
	sub_board = board[play_row][play_col]

	for row_num in range(3):
		for col_num in range(3):
			# if empty
			if sub_board[row_num][col_num] == '0':

				if sub_board_is_full(board, row_num, col_num) == 'E':
					valid_moves[row_num][col_num] = 2
				else:
					valid_moves[row_num][col_num] = 1
			else:
				valid_moves[row_num][col_num] = 0

	return valid_moves


# returns the character of who won the game
# return the '0' character if no one has won yet
# returns 'F' if board was full, and no one has won.
def who_won(board):

	result_board = [[sub_board_is_full(board,x,y) for x in range(3)] for y in range(3)]

	if (result_board[0][0] == result_board[0][1] and result_board[0][1] == result_board[0][2]):
		return result_board[0][0];
	if (result_board[1][0] == result_board[1][1] and result_board[1][1] == result_board[1][2]):
		return result_board[1][0];
	if (result_board[2][0] == result_board[2][1] and result_board[2][1] == result_board[2][2]):
		return result_board[2][0];

	# horizontal
	if (result_board[0][0] == result_board[1][0] and result_board[1][0] == result_board[2][0]):
		return result_board[0][0];
	if (result_board[0][1] == result_board[1][1] and result_board[1][1] == result_board[2][1]):
		return result_board[0][1];
	if (result_board[0][2] == result_board[1][2] and result_board[1][2] == result_board[2][2]):
		return result_board[0][2];

	# diagonals
	if (result_board[0][0] == result_board[1][1] and result_board[1][1] == result_board[2][2]):
		return result_board[0][0];
	if (result_board[2][0] == result_board[1][1] and result_board[1][1] == result_board[0][2]):
		return result_board[2][0];

	for row in result_board:
		for char in row:
			if char == '0':
				return char

	return 'F'



















