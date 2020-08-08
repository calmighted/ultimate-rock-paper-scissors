
winning_combos = {
	'rock': ('fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'),
	'fire': ('scissors','', 'snake', 'human', 'tree', 'wolf', 'sponge'),
	'scissors': ('snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'),
	'snake': ('human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'),
	'human': ('tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'),
	'tree': ('wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'),
	'wolf': ('sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'),
	'sponge': ('paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'),
	'paper': ('air', 'water', 'dragon', 'devil', 'lightning', 'gun','rock'),
	'air': ('water', 'dragon', 'devil', 'lightning', 'gun','rock','fire'),
	'water': ('dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'),
	'dragon': ('devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'),
	'devil': ('lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'),
	'lightning': ('gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'),
	'gun': ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf')
}
all1 = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
       'devil', 'lightning', 'gun')

import random
name = input('Enter your name:')
print("hello, {}".format(name))
d = {}
move_choices = input("what choices do you want to have, press ENTER to have default or any other options separated with (,):")
move_choices = list(move_choices.split(",")) 
with open("/Users/your_name/Desktop/rock-paper/rating.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = int(val)
'''{'Tim': 350, 'Jane': 200, 'Alex': 400}'''
if name not in d:
    score = 0
elif name in d:
	score = d[name]

if move_choices == ['']:
	print('Okay, let\'s start')
	move_choices = ['rock', 'paper','scissors']
	game = {'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'}
	while True:
		computer = random.choice(['rock', 'paper', 'scissors'])
		user = input()
		if user == '!exit':
			print('Bye!')
			quit()
		if user == computer:
			print('There is a draw ({})'.format(user))
			score += 50
		elif game[computer] == user:
			print('Well done. Computer chose {} and failed'.format(computer))
			score += 100
		elif user == '!rating':
			print('Your rating: {}'.format(score))
		elif user not in game:
			print('Invalid input')
		elif game[computer] != user:
			print('Sorry, but computer chose {}'.format(computer))

	
print('Okay, let\'s start')	
while True:
	user = input()
	computer = random.choice(move_choices)
	if user not in all1:
		if user == '!exit':
			print('Bye!')
			break
		elif user == '!rating':
			print('Your rating: {}'.format(score))
		else:
			print('Invalid input')
	# if user == '!exit':
	# 	print('Bye!')
	# 	break	
	if user == computer:
		print('There is a draw ({})'.format(computer))
		score += 50
	elif user in winning_combos[computer]:
		print('Sorry, but computer chose {}'.format(computer)) #computer wins
	else: #computer not in winning_combos[user]:
		print('Well done. Computer chose {} and failed'.format(computer))
		score += 100
	# elif user == '!rating':
	# 	print(score)	
	# elif user not in all1:
