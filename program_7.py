from datetime import datetime
import board_utils

TOP_LEVEL = 7
MIDDLE = 40

def empty(a):
	if type(a) == list:
		for i in a:
			empty(i)
	else:
		if a != 0:
			return False
	return True


def get_move(time, string):
	dt = datetime.now()
	us = string[0]
	where_move = string[1]
	board = [[[[0]* 3]*3]*3]*3
	print(board)
	for i in range(3):
		for j in range(3):
			for k in range(3):
				for l in range(3):
					print i, j, k , l
					board[i][j][k][l] = string[27*i + 9*j + 3*k + l + 2]
	board_utils.printboard(board)
	if empty(board):
		return MIDDLE
	return "0" #bestmove


'''
def best_move(us, turn, move, board):
	return 0

def minimax(level, time_left, us, turn, move, board):
	if level == 0:
		return algorithm(move, turn, us, board)
	elif terminal(board):
		return tie_count_wins(us, board)
	elif turn == us:
		best_val = -1000000
		moves = find_moves(turn, move, board)
		if TOP_LEVEL  - 2 >= 
	else:
		best_val = 1000000
		moves = find_moves(turn, move, board)
'''