class player:
	
	# Preset attributes
	health = 20
	
	# Attributes to be set during object creating
	def __init__(self, name):
		self.name = name

	# Methods
	def hpchange(self, hp):
		self.health = self.health + hp
		if self.health > 0:
			print(f'Health left: {self.health}')

	def dead(self):
		print(
			f'You ran out of health, {self.name}.'
			'\nYour legs start to turn soft as you fall to the ground.'
			'\nIn a matter of seconds, you lost all consciousness.'
			)