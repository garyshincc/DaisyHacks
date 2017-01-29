
from pprint import pprint
from copy import deepcopy
emptynum = 0

def opposite(currColour):
	if currColour == 1:
		return 2
	return 1

def algorithm(board, move, currColour, us):
	boardCheckResult = sub_board_is_full(board, move)

	if boardCheckResult == '0':
		return getScore(board, move, us)

	#We would have to make a bad move, by sending the opponent to a full or won section
	if currColour == us:
		return -1000000

	#the opponent would make a bad move by sending us to a full or won section
	else:
		return 1000000

def sub_board_is_full(board, move):
	play_col = move % 3
	play_row = move / 3
	sub_board = board[play_row][play_col]
	# vertical
	if (sub_board[0][0] == sub_board[0][1] and sub_board[0][1] == sub_board[0][2] and sub_board[0][0] != emptynum):
		return sub_board[0][0]
	if (sub_board[1][0] == sub_board[1][1] and sub_board[1][1] == sub_board[1][2] and sub_board[1][0] != emptynum):
		return sub_board[1][0]
	if (sub_board[2][0] == sub_board[2][1] and sub_board[2][1] == sub_board[2][2] and sub_board[2][0] != emptynum):
		return sub_board[2][0]

	# horizontal
	if (sub_board[0][0] == sub_board[1][0] and sub_board[1][0] == sub_board[2][0] and sub_board[0][0] != emptynum):
		return sub_board[0][0]
	if (sub_board[0][1] == sub_board[1][1] and sub_board[1][1] == sub_board[2][1] and sub_board[0][1] != emptynum):
		return sub_board[0][1]
	if (sub_board[0][2] == sub_board[1][2] and sub_board[1][2] == sub_board[2][2] and sub_board[0][2] != emptynum):
		return sub_board[0][2]

	# diagonals
	if (sub_board[0][0] == sub_board[1][1] and sub_board[1][1] == sub_board[2][2] and sub_board[1][1] != emptynum):
		return sub_board[0][0]
	if (sub_board[2][0] == sub_board[1][1] and sub_board[1][1] == sub_board[0][2] and sub_board[1][1] != emptynum):
		return sub_board[2][0]

	for row in sub_board:
		for char in row:
			if char == emptynum:
				return char

	return 'F'

def copy_board(board):
	new_board = deepcopy(board)
	return new_board

def sub_board_win(sub_board, move, player):
	s_board = copy_board(sub_board)
	checkRow = move / 3
	checkCol = move % 3
	s_board[checkRow][checkCol] = player
	# vertical
	if (s_board[0][0] == s_board[0][1] and s_board[0][1] == s_board[0][2] and s_board[0][0] == player):
		return True
	if (s_board[1][0] == s_board[1][1] and s_board[1][1] == s_board[1][2] and s_board[1][0] == player):
		return True
	if (s_board[2][0] == s_board[2][1] and s_board[2][1] == s_board[2][2] and s_board[2][0] == player):
		return True

	# horizontal
	if (s_board[0][0] == s_board[1][0] and s_board[1][0] == s_board[2][0] and s_board[0][0] == player):
		return True
	if (s_board[0][1] == s_board[1][1] and s_board[1][1] == s_board[2][1] and s_board[0][1] == player):
		return True
	if (s_board[0][2] == s_board[1][2] and s_board[1][2] == s_board[2][2] and s_board[0][2] == player):
		return True

	# diagonals
	if (s_board[0][0] == s_board[1][1] and s_board[1][1] == s_board[2][2] and s_board[1][1] == player):
		return True
	if (s_board[2][0] == s_board[1][1] and s_board[1][1] == s_board[0][2] and s_board[1][1] == player):
		return True

	return False

def getScore(board, move, us):
	# move duals as location
	location = move
	pointTotal = 1
	if move == 9:
		return -25
	if sub_board_is_full(board,move):
		return -25
	checkRow = move / 3
	checkCol = move % 3
	sub_board = board[checkRow][checkCol]

	
	for k2 in range(3):
		for l2 in range(3):

			curr = sub_board[k2][l2]
			if curr == us:
				if k2 == 1 and l2 == 1:
					pointTotal += 1

				elif (k2+l2) % 2 == 0:
					pointTotal += 3

				else:
					pointTotal += 5

			elif curr == opposite(us):
				if k2 == 1 and l2 == 1:
					pointTotal -= 1
				elif (k2+l2) % 2 == 0:
					pointTotal -= 3
				else:
					pointTotal -= 5

			if sub_board_win(sub_board,move,curr):
				pointTotal += 50
			if sub_board_win(sub_board,move,opposite(curr)):
				pointTotal -= 50

	if checkRow == 1 and checkCol == 1:
		pointTotal *= 2
	# corners
	elif (checkRow + checkCol) % 2 == 0:
		pointTotal *= 6
	# edges		
	else:
		pointTotal *= 4


	return pointTotal

class square:
	def __init__(self,ID,val):
		self.ID = ID
		self.value = val
		self.bigSq = self._getbigSq()
		self.smallSq = self._getsmallSq()
	def _getbigSq(self):
		#return 3*int(self.ID/27) + int((self.ID%9)/3)
		return int(self.ID/9)
	def _getsmallSq(self):
		return self.ID%9

def printboard(board):
	for i in range(3):
		for k in range(3):
			for j in range(3):
				for l in range(3):
					print str(board[i][j][k][l]),
				print " ",
			print " "
		print " "


def findValidMoves(squares,nextsquare):
	vm = []
	for i in range(81):
		if squares[i].bigSq==nextsquare or nextsquare>8:  #Have to play in the next square, unless you can play anywhere
			if squares[i].value == 0: #Square must be empty
				if isBoardWon(getBigBoard(squares,squares[i].bigSq))==0: #Can't play in a won board
					if not isBoardFull(getBigBoard(squares,squares[i].bigSq)): #Can't play in a full board
						vm.append(i)
	return vm

def isBoardWon(squares):
        #Input: squares = 8 item list of squares 
        #Output: 0 if not win, 1 if 1 won, 2 if 2 won
	def compareSquares(squares,s1,s2,s3,v):
		if squares[s1]==squares[s2] and squares[s1]==squares[s3] and squares[s1]==v:
			return True
		else:
			return False
	if compareSquares(squares,0,1,2,1): return 1
	if compareSquares(squares,0,1,2,2): return 2
	if compareSquares(squares,3,4,5,1): return 1
	if compareSquares(squares,3,4,5,2): return 2
	if compareSquares(squares,6,7,8,1): return 1
	if compareSquares(squares,6,7,8,2): return 2
	if compareSquares(squares,0,3,6,1): return 1
	if compareSquares(squares,0,3,6,2): return 2
	if compareSquares(squares,1,4,7,1): return 1
	if compareSquares(squares,1,4,7,2): return 2
	if compareSquares(squares,2,5,8,1): return 1
	if compareSquares(squares,2,5,8,2): return 2
	if compareSquares(squares,0,4,8,1): return 1
	if compareSquares(squares,0,4,8,2): return 2
	if compareSquares(squares,2,4,6,1): return 1
	if compareSquares(squares,2,4,6,2): return 2
	return 0

def isBoardFull(squares):
	for i in range(9):
		if squares[i]==0:
			return False
	return True

def getBigBoard(squares,bigSq):
	sq = []
	for i in range(81):
		if squares[i].bigSq == bigSq:
			sq.append(squares[i].value)
	return sq

def get_move(timeout,data):
	PLAYER=int(data[0])
	nextsquare=int(data[1])
	squares = []
	for i in range(2,83):
		squares.append(square(i-2,int(data[i])))
	validMoves=findValidMoves(squares,nextsquare)
	board = [[[[2 for x in range(3)] for y in range(3)] for z in range(3)] for k in range(3)]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				for l in range(3):
					board[i][j][k][l] = squares[l + 3*k + 9*j + 27*i].value

	printboard(board)
	if nextsquare == 9:
		# valid moves are lots
		# return something
		pass

	# valid move is not free
	best_score = -1000
	best_move = 0

	for move_num in range(len(validMoves)):
		temp = getScore(board,validMoves[move_num]%9, PLAYER)
		
		if move_num % 9 == 4 and nextsquare == 4:
			temp += 5000
		print temp
		if best_score < temp:
			best_score = temp
			best_move = validMoves[move_num]

	print validMoves
	return best_move

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




if __name__ == '__main__':
	print(get_move(10, "11111000000000000011221000000000000000000000000000000000000000000000000000000000000"))


