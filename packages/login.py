from packages import playerinfo

def ageCheck():
    while True:
        
        e = input(
            'Welcome to Dungeon v1.0!\n'
            'You have to be 16+ to play this game. Enter "CONFIRM" : '
            )
        
        if e.lower() == 'confirm':
            break
        
        else:
            print('Goodbye.')
            exit()

def newgame():
	e = input('Please enter your name: ')
	player = playerinfo.player(e)
	print(f'Welcome to the dungeon, {player.name}!')
	return player

def main():
	while True:
		
		try:
			e = int(
					input(
					'\nDungeon v1.0\n'
					'--------------\n'
					'1. New Game\n'
					'0. Quit\n'
					'Your choice: '
						)
					)
			
			if e == 1:
				return newgame()
			elif e == 0:
				exit()

			else:
				raise ValueError
		except ValueError:
			print('Invalid input. Try again.')
