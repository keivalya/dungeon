from packages import login, playerinfo, questions

def dungeon(player):
    for k, v in questions.questions.items():
        print()
        print(k)
        for i in range(len(v[0])):
            print('{}. {}'.format(i+1, v[0][i]))
        try:
            e = int(input('Your Choice: ')) - 1
            if e in range(len(v[0])):
                print(v[1][e])
                hp = v[2][e]
                player.hpchange(hp)
                if player.health > 0:
                    input('Press <ENTER> to proceed.')
                else:
                    player.dead()
                    break
            else:
                raise ValueError
        except ValueError:
            pass

def gameover(player):
    print('Game Over!')
    if player.health > 0:
        print("You Survived! Good End.")
    else:
        print("You're dead. Bad End.")
    input('<Enter> to return to menu.')

def main():
    login.ageCheck()
    while True:
        player = login.main()
        dungeon(player)
        gameover(player)

main()
