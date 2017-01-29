from datetime import datetime
import board_utils
import numpy
import random
from copy import copy, deepcopy

TOP_LEVEL = 4
MIDDLE = 40



def algorithm(board, move, currColour, us):
    boardCheckResult = sub_board_is_full(board, move)

    if boardCheckResult == '0':
        return getScore(board, move, currColour, us)

    #We would have to make a bad move, by sending the opponent to a full or won section
    if currColour == us:
        return -1000000

    #the opponent would make a bad move by sending us to a full or won section
    else:
        return 1000000

def getScore(board, checkRow, checkCol, currColour, us):
    pointTotal = 0;
    for k2 in range(3):
        for l2 in range(3):

          curr = board[checkRow][checkCol][k2][l2]

          if curr == us:
            if k2 == 1 and l2 == 1:
              pointTotal += 5
            elif (k2+l2) % 2 == 0:
              pointTotal += 3;
            else:
              pointTotal += 1;
          elif curr == opposite(us):
            if k2 == 1 and l2 == 1:
              pointTotal -= 5;
            elif (k2+l2) % 2 == 0:
              pointTotal -= 3;
            else:
              pointTotal -= 1;


          #printf("%c  %d\n", curr, pointTotal);

    return pointTotal;


def empty(a):
	if type(a) == list:
		for i in a:
			if not empty(i):
				return False
	else:
		if a != 0:
			return False
	return True

def get_move(time, string):
	dt = datetime.now()
	us = int(string[0])
	where_move = int(string[1])

	board = [[[[0 for x in range(3)] for y in range(3)] for z in range(3)] for k in range(3)]

	for i in range(3):
		for j in range(3):
			for k in range(3):
				for l in range(3):
					board[i][j][k][l] = int(string[27*i + 9*j + 3*k + l + 2])
	board_utils.printboard(board)
	if empty(board):
		print 
		return MIDDLE
	return  0 #bestmove(us, dt, move, board)

	#return x, y #false is small, true is big
'''def monte_carlo(is_free, valid_moves):
	if is_free:
		return valid_moves
	else:
		for i in range(3):
			for j in range(3):
				if valid_moves[i][j] == 2 and not random.getrandbits(1): # makes python get a random bool
					valid_moves[i][j] = 3

def copy_board(board):
	new_board = deepcopy(board)
	return new_board



def best_move(us, time, move, board):
	# is_free is when the move was a 9-type.
	# returning True, and a 4D 3x3x3x3 array
	# otherwise returns False, and returns 2D 3x3 array
	# 3 is available but suppressed by monte carlo
	# 2 is available,
	# 1 is available but gives a free move,
	# 0 is someone is already there

	is_free, valid_moves = board_utils.get_valid_moves(board, move)
	maximum = -1000000
	bestmove = -1
	move_counter = 0
	if(is_free):
		for i in range(3):
			for j in range(3):
				for k in range(3):
					for l in range(3):
						if(valid_moves[i][j][k][l] == 2):
							move_counter+=1
							new_board = copy_board(board)
							new_board[i][j][k][l] = us  #made the move
							current_score = minimax(TOP_LEVEL, time, us, us, move, new_board)
							if current_score > maximum:
								bestmove = 27*i + 9*j + 3*k + l
								maximum = current_score

	else:
		i = move / 3
		j = move % 3
		move_counter = 0
		for k in range(3):
			for l in range(3):
				if valid_moves[k][l] == 2:




def minimax(level, time_left, us, turn, move, board):
	if level == 0:
		return algorithm(move, turn, us, board)
	elif terminal(board):
		return tie_count_wins(us, board)
	elif turn == us:
		best_val = -1000000
		is_free, valid_moves = board_utils.get_valid_moves(board, move)
		monte_carlo(is_free, valid_moves)
		if is_free: 
			for i in range(3):
				for j in range(3):
					for k in range(3):
						for l in range(3):

	else:
		best_val = 1000000
		moves = find_moves(turn, move, board)
'''
