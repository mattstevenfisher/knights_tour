def get_valid_moves(board, x, y):
	xpos = [1, -1, -1,  1, 2, -2, -2,  2]
	ypos = [2,  2, -2, -2, 1,  1, -1, -1]

	moves = zip([x + d for d in xpos], [y + d for d in ypos])
	valid_moves = []
	for i in range(len(moves)):
		if (0 <= moves[i][0] < len(board)) and (0 <= moves[i][1] < len(board)) and (board[moves[i][0]][moves[i][1]] == 0):
			valid_moves.append(moves[i])
	return valid_moves


def move_knight(boards, in_board, x, y):
	boards.update({(x,y): list(in_board)})
	board = boards[x,y]
	board[x][y] = len(boards)

	print_board(board)
	print len(boards)
	print x,y
	print get_valid_moves(board, x, y)

	if max(max(board)) == len(board)*len(board):
		return board
	else:
		pos_moves = get_valid_moves(board, x, y)
		for i in range(len(pos_moves)):
			print pos_moves[i]
			soln = move_knight(boards, board, pos_moves[i][0], pos_moves[i][1])
			if max(max(soln)) == len(board)*len(board):
				return soln
		return boards.pop((x,y))


def print_board(board):
	for i in range(len(board)):
		print board[i]
	print ''



def solve_knights_tale(size):
	if size < 6:
		print "Board size too small.  No solutions exist for a {0}x{0} chess board.".format(size)
		return
	else:
		print "Solving knight's tale..."
		boards = {}

		xlim = size/2 + size%2
		ylim = size/2

		for x in range(xlim):
			for y in range(xlim):
				soln = move_knight(boards, [[0]*size for i in range(size)], x, y)
				print_board(soln)
				if max(max(soln)) == size*size:
					break
			if max(max(soln)) == size*size:
				print 'Solution found.'
				print_board(board)
				break
		print 'No solution found.'
	pass







# size = 6
# board = [[0]*size for i in range(size)]
# print get_valid_moves(board, 1, 2)
solve_knights_tale(6)