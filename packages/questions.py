'''Format of questions:
Question
(choice1, choice2, ...)
(result1, result2, ...)
(hpchange1, hpchange2, ...)
'''

questions = {
	"First choice... Left or Right?" : [
	('left', 'right'),
	('Walking...', "You fell down into a well, blind person! You lost"),
	(0, -20)
	],
	
	"Alright! Now you followed the path, exhausted, you walk and reach out to a lake.\n"
	"You quenched your thirst. Do you swim across or go around?" : [
	('around', 'across'),
	("You are a wise person choosing a looooooooong way to reach his destination. Hardwork always pays off. You went around and reached the other side of the lake.", "Swimmer! Unfortunately, you were caught into a deadly battle with a crocodile! Your health is halved."),
	(0, -10)
	],

	"You notice a house and a river. Which do you go to? " : [
	('house', 'river'),
	("You go to the house and are greeted by a beautiful mistress... She doesn't like the way you behave and you lose 5 health", "Ohhh water entered into boat!"),
	(-5, -20)
	],

	}