from info import PlayerInfo as info
from Game import Game as game

print("DUNGEON GAME!\n Make your choices, well")
class Flow:

    def main(self):
        """
        Main Method will drive all operations.
        :return:
        Fun ;)
        """
        _age = info.getInfo(self)
        _flag = game.check_age(self, _age)
        if _flag == False:
            exit()
        game.wants_to_play(0)

"""
Here object created and and called main method
"""
ObjFlow = Flow()
ObjFlow.main()
