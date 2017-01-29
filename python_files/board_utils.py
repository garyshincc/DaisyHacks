import sys
from pprint import pprint 

def opposite(currColour):
    if currColour == '1':
        return '2'
    return '1'
	
# this will check if the entire 9x9 board is full.
emptynum = 0

def board_is_full(board):
	for sub_row in board:
		for sub_board in sub_row:
			for row in sub_board:
				for char in row:
					if char == emptynum:
						return False

	return True

# this will check if a sub board is playable.
# returns characters
# will return the color that the board is owned by,
# if tied in that board, it will return 'E'
# if board is full it will return 'F'
def sub_board_is_full(board, move):

	play_col = move % 3
	play_row = move / 3
	sub_board = board[play_row][play_col]
	# vertical
	if (sub_board[0][0] == sub_board[0][1] and sub_board[0][1] == sub_board[0][2] and sub_board[0][0] != emptynum):
		return sub_board[0][0];
	if (sub_board[1][0] == sub_board[1][1] and sub_board[1][1] == sub_board[1][2] and sub_board[1][0] != emptynum):
		return sub_board[1][0];
	if (sub_board[2][0] == sub_board[2][1] and sub_board[2][1] == sub_board[2][2] and sub_board[2][0] != emptynum):
		return sub_board[2][0];

	# horizontal
	if (sub_board[0][0] == sub_board[1][0] and sub_board[1][0] == sub_board[2][0] and sub_board[0][0] != emptynum):
		return sub_board[0][0];
	if (sub_board[0][1] == sub_board[1][1] and sub_board[1][1] == sub_board[2][1] and sub_board[0][1] != emptynum):
		return sub_board[0][1];
	if (sub_board[0][2] == sub_board[1][2] and sub_board[1][2] == sub_board[2][2] and sub_board[0][2] != emptynum):
		return sub_board[0][2];

	# diagonals
	if (sub_board[0][0] == sub_board[1][1] and sub_board[1][1] == sub_board[2][2] and sub_board[1][1] != emptynum):
		return sub_board[0][0];
	if (sub_board[2][0] == sub_board[1][1] and sub_board[1][1] == sub_board[0][2] and sub_board[1][1] != emptynum):
		return sub_board[2][0];

	for row in sub_board:
		for char in row:
			if char == emptynum:
				return char

	return 'F'


def printboard(board):
	for i in range(3):
		for k in range(3):
			for l1 in range(3):
				sys.stdout.write(str(board[i][0][k][l1]) + ' ')
			sys.stdout.write('  ')
			for l2 in range(3):
				sys.stdout.write(str(board[i][1][k][l2]) + ' ')
			sys.stdout.write('  ')
			for l3 in range(3):
				sys.stdout.write(str(board[i][2][k][l3]) + ' ')

			print
		print

# returns a 2-D array of valid moves
# the array will be 3 by 3 size type int
# play row and play col correspond to which sub_board
# is to be played currently.


# if move is 0 to 8, then returns false, and a 2D 3 by 3 array
# if move is 9, then returns true, and returns a 4D 3x3x3x3 array
# 2 is available,
# 1 is available but undesireable,
# 0 is impossible
def get_valid_moves(board, move):
	if move == 9:
		valid_moves = [[[[2 for x in range(3)]for y in range(3)] for j in range(3)] for k in range(3)]
		for board_row_num in range(3):
			for board_col_num in range(3):

				# removes already played positions
				sub_board = board[board_row_num][board_col_num]
				for row_num in range(0,3):
					for col_num in range(0,3):
						# if the position is already taken
						if sub_board[row_num][col_num] != emptynum:
							valid_moves[board_row_num][board_col_num][row_num][col_num] = 0
						
						# if the position is playable,
						if sub_board[row_num][col_num] == emptynum:
							next_sub_move = row_num + (3 * col_num)
							# if the leading sub_board is won/full
							if sub_board_is_full(board, next_sub_move) != emptynum:
								valid_moves[board_row_num][board_col_num][row_num][col_num] = 1
				
				# checks if the board is done playing. i.e. full or won
				next_move = board_row_num + 3*board_col_num
				if sub_board_is_full(board, next_move) != emptynum:
					for row_num in range(3):
						for col_num in range(3):
							valid_moves[board_row_num][board_col_num][row_num][col_num] = 0
		for i in range(3):
			for j in range(3):
				valid_moves[i][j] = zip(*valid_moves[i][j])
		valid_moves = zip(*valid_moves)
		return True, valid_moves


	play_row = move / 3
	play_col = move % 3

	valid_moves = [[2 for x in range(3)] for y in range(3)]

	sub_board = board[play_row][play_col]

	for row_num in range(3):
		for col_num in range(3):
			# if empty
			if sub_board[row_num][col_num] == emptynum:

				if sub_board_is_full(board, move) == emptynum:
					valid_moves[row_num][col_num] = 2
				else:
					valid_moves[row_num][col_num] = 1
			else:
				valid_moves[row_num][col_num] = 0

	return False, valid_moves


# returns the character of who won the game
# return the '0' character if no one has won yet
# returns 'F' if board was full, and no one has won.
def who_won(board):

	result_board = [[sub_board_is_full(board, x + 3*y) for x in range(0,3)] for y in range(0,3)]


	if (result_board[0][0] == result_board[0][1] and result_board[0][1] == result_board[0][2] and sub_board[0][0] != emptynum):
		return result_board[0][0];
	if (result_board[1][0] == result_board[1][1] and result_board[1][1] == result_board[1][2] and sub_board[1][0] != emptynum):
		return result_board[1][0];
	if (result_board[2][0] == result_board[2][1] and result_board[2][1] == result_board[2][2] and sub_board[2][0] != emptynum):
		return result_board[2][0];

	# horizontal
	if (result_board[0][0] == result_board[1][0] and result_board[1][0] == result_board[2][0] and sub_board[0][0] != emptynum):
		return result_board[0][0];
	if (result_board[0][1] == result_board[1][1] and result_board[1][1] == result_board[2][1] and sub_board[0][1] != emptynum):
		return result_board[0][1];
	if (result_board[0][2] == result_board[1][2] and result_board[1][2] == result_board[2][2] and sub_board[0][2] != emptynum):
		return result_board[0][2];

	# diagonals
	if (result_board[0][0] == result_board[1][1] and result_board[1][1] == result_board[2][2] and sub_board[1][1] != emptynum):
		return result_board[0][0];
	if (result_board[2][0] == result_board[1][1] and result_board[1][1] == result_board[0][2] and sub_board[1][1] != emptynum):
		return result_board[2][0];

	for row in result_board:
		for num in row:
			if num == emptynum:
				return num

	# return 3 if full
	return 3


'''
# test code
test_board = [[[[emptynum for x in range(3)] for y in range(3)] for z in range(3)] for k in range(3)]

test_board[1][1][0][0] = 'O'
test_board[1][1][1][1] = 'O'
test_board[1][1][2][2] = 'X'

test_board[0][2][0][0] = 'X'
test_board[0][2][1][1] = 'X'
test_board[0][2][2][2] = 'O'

test_board[2][0][0][0] = 'O'
test_board[2][0][1][1] = 'O'
test_board[2][0][2][2] = 'O'

printboard(test_board)

is_free, valid_moves = get_valid_moves(test_board,9,'W')
for i in range(3):
	for j in range(3):
		valid_moves[i][j] = zip(*valid_moves[i][j])
valid_moves = zip(*valid_moves)
printboard(valid_moves)

is_free, valid_moves = get_valid_moves(test_board,2,'W')

for i in range(3):
	for j in range(3):
		sys.stdout.write(str(valid_moves[i][j]) + ' ')
	print
'''


