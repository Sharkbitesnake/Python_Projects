#GHOST GAME#
from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
	ghost_door = randint(1,3)
	print('Three doors ahead...')
	print('A ghost behind one.')
	print('Which one do you open?')
	chosen_door = int(input('1, 2 or 3? '))
	if chosen_door == ghost_door:
		print('GHOST!')
		feeling_brave = False
	else:
		print('No Ghost!')
		print('You enter the next room')
		score = score + 1
print('Run away!')
print('Game over! You scored', score)