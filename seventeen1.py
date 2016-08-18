import random 

def read_file():
	"""Reads in input file. Returns list of lists of sequences.
	"""
	lines_list = []
	with open('i206_placein_output1_<anna.cho>.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			words = line.split(',')
			lines_list.append(words)
	return lines_list


# If the number of marbles left in the jar is fewer than the next number in the play sequence, 
# then Player 1 should remove all the remaining marbles.
def player1(lst, round, index, marbles_left):
	"""Player 1 chooses the next number in the sequence of the output file from pervious
	version of game.
	"""
	p1_choice = lst[round][index]
	p1_choice = int(p1_choice)
	if p1_choice > marbles_left:
		p1_choice = marbles_left
	return p1_choice	

# Player 2 will play the same marble-removal strategy as in Version 1.
def player2(marbles_left):
	"""Computer randomly choices its selection. 
	"""
	max = 3
	if marbles_left < 3:
		max = marbles_left
	p2_choice = random.randint(1, max)
	return p2_choice

# The program will play the game as many times as there are lines in the input file, 
# printing the sequence of moves 
# and the game winner into an output text file (named i206_placein_output2_<ischool_userid>.txt'), 
# one line per game.
def gameplay():
	lst = read_file()
	total_games = len(lst)
	game = 0
	p1_wins = 0
	p2_wins = 0
	with open('i206_placein_output2_<anna.cho>.txt', 'w') as fout:
		for n in range(total_games):
			marbles_left = 17
			fout.write('Game #{}. Play sequence: '.format(game + 1))
			while marbles_left != 0:
				p1_choice = player1(lst, n, 0, marbles_left)
				marbles_left -= p1_choice
				if marbles_left == 0:
					fout.write(str(p1_choice) + '. Winner: P2\n')
					p2_wins += 1
					break
				else:
					fout.write(str(p1_choice) + '-')
				p2_choice = player2(marbles_left)
				marbles_left -= p2_choice
				if marbles_left == 0:
					fout.write(str(p2_choice) + ', Winner: P1\n')
					p2_wins += 1
					break
				else:
					fout.write(str(p2_choice) + '-')
		fout.write('Player 1 won {} times; Player 2 won {} times'.format(p1_wins, p2_wins))

# At the end of all the games, the program will print the number of games won by each player. 

def main():
	gameplay()

if __name__ == '__main__':
	main()
