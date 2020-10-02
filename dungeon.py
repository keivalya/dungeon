def quest(quest,options,answer):
    print(quest)
    for v in options:
        print v
    if(input("what would you choose ?  ")==answer):
        print('congrats')
    else:
        print('next luck next Time')
     

print("DUNGEON GAME! Make your choices, well")

name= input("Hey! What's yout name? ")
age = int(input("How old are you? "))

print("Namaste", name, "so you're", age, "huh!")

health = 20

print("You are starting with", health, "health")

if age>=16:
    print("welcome! You're old enough to play!")

    wants2play = input("Do you want to play? ").lower()
    if wants2play == "yes":
        print("Let's PLAY!")
        lor = input("First choice... Left or Right (left/right)?").lower()
        if lor =="left":
            ans = input("Alright! Now you followed the path, exhausted, you walk and reach out to a lake. You quench your thirst. Do you swim across or go around (across, around)?").lower()

            if ans == "around":
                print("You are a wise person choosing a looooooooong way to reach his destination. Hardwork always pays off. You went around and reached the other side of the lake.")
            elif ans == "across":
                print("Swimmer! Unfortunately, you were caught into a deadly battle with a crocodile! Your health is halved.")
                health -= 10

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by a beautiful mistress... She doesn't like the way you behave and you lose 5 health")
                health -= 10

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived ... You win!")

            else:
                print("You lost dummy. This is not even a choiceee!!")
        else:
            print("You fell down into a well, blind person! You lost")

    else:
        print("Well, see ya soon!")
    
else:
    print("You're not old enough. SORRY :(")
    print('But your are welcome to retunr when you have the age")
