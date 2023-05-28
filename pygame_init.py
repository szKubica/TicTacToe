import sys

class Game:
	def __init__(self, size):
		self.size = size
		self.empty_symbol = '□'
		self.board = [[self.empty_symbol for _ in range(
		    self.size)] for _ in range(self.size)]
		self.player_symbol = 'o'
		self.computer_symbol = 'x'

	def draw(self):
		for row in self.board:
			print(' '.join(row))

	def is_free(self, pos):
		if self.board[int(pos[1])-1][int(pos[0])-1] == self.empty_symbol:
			return True
		return False

	def set_player(self):
		pos = input('Enter coordinates separaed by space ').split()
		if self.is_free(pos):
			self.board[int(pos[1]) - 1][int(pos[0]) - 1] = self.player_symbol
			self.draw()
			self.check_win(self.player_symbol)
		else:
			print('Given place is not empty, enter valid coordinates again')
			self.set_player()
		if self.check_tie(self.player_symbol):
			print('Player won')
			
	def check_win(self, symbol):
		for i in range(self.size):
			if all(self.board[i][j] == symbol for j in range(self.size)):
					return True
			if all(self.board[j][i] == symbol for j in range(self.size)):
					return True
		if all(self.board[i][i] == symbol for i in range(self.size)):
				return True
		if all(self.board[i][self.size - i - 1] == symbol for i in range(self.size)):
				return True
		return False

	def check_tie(self):
		for x in self.board:
			for y in x:
				if y == self.empty_symbol:
					return False
		return True
	
	def min_max(self, board, is_maximing, alpha, beta, depth):
			if self.check_win(self.computer_symbol):
					return 1
			elif self.check_win(self.player_symbol):
					return -1
			elif self.check_tie():
					return 0
			elif depth == 0:
					return 0
					
			if is_maximing:
					best_score = -1000
					for x in range(self.size):
							for y in range(self.size):
									if board[x][y] == self.empty_symbol:
											board[x][y] = self.computer_symbol
											score = self.min_max(board, False, alpha, beta, depth-1)
											board[x][y] = self.empty_symbol
											best_score = max(best_score, score)
											alpha = max(alpha, best_score)
											if beta <= alpha: 
													break
					return best_score

			else:
					best_score = 1000
					for x in range(self.size):
							for y in range(self.size):
									if board[x][y] == self.empty_symbol:
											board[x][y] = self.player_symbol
											score = self.min_max(board, True, alpha, beta, depth-1)
											board[x][y] = self.empty_symbol
											best_score = min(best_score, score)
											beta = min(beta, best_score)
											if beta <= alpha:
													break	
					return best_score

	def set_computer(self):
			best_score = -1000
			best_move = []
			alpha = -1000
			beta = 1000
			for x in range(self.size):
				for y in range(self.size):
					if self.board[x][y] == self.empty_symbol:
						self.board[x][y] = self.computer_symbol
						score = self.min_max(self.board, False, alpha, beta, 6)
						self.board[x][y] = self.empty_symbol
						if score > best_score:
							best_score = score
							best_move = [x, y]
						alpha = max(alpha, best_score)
						if beta <= alpha:
							break
			self.board[int(best_move[0])][int(best_move[1])] = self.computer_symbol
			self.draw()
			if self.check_win(self.computer_symbol):
				print('Computer won')
				sys.exit() 
			if self.check_tie():
				print("Tie")


