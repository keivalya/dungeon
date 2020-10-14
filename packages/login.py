class Player:
	
	def __init__(self, name):
		self.name = name

	def hpchange(self, hp):
		self.health = self.health + hp
		if self.health > 0:
			return True
		else:
			return False

def newPlayer():
	"""
	THIS FUNCTION CHECK IF PLAYER IS 16+ AND ASKS FOR PLAYER NAME.
	"""
	while True:
		e = input("You need to be 16+ to proceed. Confirm (Y/N)? ").lower()
		if e == "y":
			break
		elif e == "n":
			exit()

	while True:
		e = input("Hi Traveller! How should I address you : ")
		if e:
			return Player(e)
		else:
			print("You cannot leave your name empty!")

# mainmenu
def menu(player):
	"""
	THIS IS THE MAIN MENU INTERFACE.
	"""
	while True:
		try:
			e = int(input(
				f"\nWelcome to DUNGEON GAME, {player.name}!\n"
				"1. New Game\n"
				"0. Quit\n"
				"Your choice: "
				))
			if e == 1:
				return player
			elif e == 0:
				exit() # exit route
			else:
				raise ValueError
		except ValueError:
			print("Invalid choice. Press <Enter> to try again.")
			input()
	
