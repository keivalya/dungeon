from packages import login, dungeon

def main():
    print("DUNGEON GAME v1.0")
    player = login.newPlayer() # Player is a class instance initiated with health = 20
    while True:
        login.menu(player)  # loop exit route available here
        dungeon.main(player) # This is the dungeon game itself (game.py)

main()