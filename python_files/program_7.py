from datetime import datetime
import board_utils

TOP_LEVEL = 7
MIDDLE = 40
emptychar = 'E'
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
			empty(i)
	else:
		if a != 0:
			return False
	return True


def get_move(time, string):
	dt = datetime.now()
	us = string[0]
	where_move = string[1]
	board = [[[[emptychar for x in range(3)] for y in range(3)] for z in range(3)] for k in range(3)]

	for i in range(3):
		for j in range(3):
			for k in range(3):
				for l in range(3):
					print i, j, k , l, string[27*i + 9*j + 3*k + l + 2]
					board[i][j][k][l] = string[27*i + 9*j + 3*k + l + 2]
					print board[i][j][k][l]
	board_utils.printboard(board)
	if empty(board):
		return MIDDLE
	return "0" #bestmove


def best_move(us, turn, move, board):
	board_utils.get_valid_moves(board, )
	algorithm()

'''
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