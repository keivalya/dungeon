from packages import login

def main(player):
    """
    THIS IS DUNGEON GAME FUNCTION.
    """
    # Give Player 20 health
    player.health = 20

    # FORKS ARE THE FORKED ROADS IN A DUNGEON
    forks = [
        
        ["First choice... Left or Right?",
        ('left', 'right'),
        ('Walking...', "You fell down into a well, blind person!"),
        (0, -20)],

        [("Alright! Now you followed the path, exhausted, you walk and reach out to a lake.\n"
            "You quenched your thirst. Do you swim across or go around?"),
        ('around', 'across'),
        ("You are a wise person choosing a looooooooong way to reach his destination.\n"
            "Hardwork always pays off. You went around and reached the other side of the lake.",
        "Swimmer! Unfortunately, you were caught into a deadly battle with a crocodile.\n"
            "Your health is halved!"),
        (0, -10)],

        ["You notice a house and a river. Which do you go to? ",
        ('house', 'river'),
        ("You go to the house and are greeted by a beautiful mistress..."
            "She doesn't like the way you behave and you lose 5 health",
        "Ohhh water entered into boat!"),
        (-5, -20)],

        ]

    # THIS IS A LOOP TO LOOP THROUGH ALL THE QUESTIONS, CHOICES AND RESULTS (FORKS CAN BE SIMPLY ADDED ABOVE)
    for fork in forks:
        question, choices, results, hp = fork
        lenChoices = len(fork[1])
        print()
        print(question)
        for i in range(lenChoices):
            print('{}. {}'.format(i+1, choices[i].title()))
        try:
            e = int(input('Your Choice: ')) - 1
            if e in range(lenChoices):
                print(results[e])
                if player.hpchange(hp[e]):
                    print(f"{player.name}, you have {player.health} HP remaining.")
                    input("Press <Enter> to proceed.")
                else:
                    print("You're dead. Gameover.")
                    input("Press <Enter> to return to MENU.")
                    return

            else:
                raise ValueError
        except ValueError:
            pass

    print("You managed to finish the dungeon, good job!")
    input("Press <Enter> to return to MENU.")