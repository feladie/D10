# Human versus computer.

import random

def human_input(marbles_left):
	"""Prompt user for input. Check whether or not input is valid.
	"""
	while True:
		try:
			human_choice = int(input('Your turn: How many marbles will you remove (1-3)? '))
		except:
			print('Sorry, that is not a valid option. Try again!')
			return 0
		else:
			if human_choice not in range(1, 4):
				print('Sorry, that is not a valid option. Try again!')
				return 0
			elif human_choice > marbles_left:
				print('Sorry, that is not a valid option. Try again!')
				return 0
			else:
				print('You removed {} marbles.'.format(human_choice))
				return human_choice

def comp_input(marbles_left):
	"""Computer randomly choices its selection. 
	"""
	max = 3
	if marbles_left < 3:
		max = marbles_left
	comp_choice = random.randint(1, max)
	print('Computer\'s turn...')
	print('Computer removed {} marbles.'.format(comp_choice))
	return comp_choice

def game_play():
	f = open('i206_placein_output1_<anna.cho>.txt', 'a')
	marbles_left = 17
	print('Let\'s play the game of Seventeen!')
	print('Number of marbles left in jar: 17')
	print('')
	while marbles_left != 0:
		human_choice = human_input(marbles_left)
		marbles_left -= human_choice
		if marbles_left == 0:
			print('\nThere are no marbles left. Computer wins!')
			f.write(str(human_choice) + '\n')
			break
		else:
			print('Number of marbles left in jar: {}\n'. format(marbles_left))
			f.write(str(human_choice) + ',')


		comp_choice = comp_input(marbles_left)
		marbles_left -= comp_choice
		if marbles_left == 0:
			print('\nThere are no marbles left. You win!')
			f.write(str(comp_choice) + '\n')
		else:
			print('Number of marbles left in jar: {}\n'. format(marbles_left))
			f.write(str(comp_choice) + ',')
	f.close()	

def main():
	game_play()

if __name__ == '__main__':
	main()