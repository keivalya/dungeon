print("DUNGEON GAME! Make your choices, well")

decisions = {
    "first_choice_left_right": None,
    "lake_around_across": None,
    "lake_river_house": None,
    "river_ride_boat": None
}

name= input("Hey! What's your name? ")
age = input("How old are you? ")

while (not age.isnumeric()) or int(age) < 0:
    age = input("That age doesn't seem right.\nCan you enter you current age?")

age = int(age)
print(f"Namaste", {name}, "so you're", {age}, "huh!")

health = 20

if age>=16:
    print("You're old enough to play!")

    wants2play = input("Do you want to play?(yes/no) ").lower()
    if wants2play == "yes":
        print("Let's PLAY!")
        print(f"You are starting with", {health}, "health points")
        decisions["first_choice_left_right"] = input("First choice... Left or Right (left/right)?").lower()
        if decisions["first_choice_left_right"] =="left":
            decisions["lake_around_across"] = input("Alright! Now you followed the path, exhausted, you walk and reach out to a lake. You quench your thirst. Do you swim across or go around (across, around)?").lower()

            if decisions["lake_around_across"] == "around":
                print("You are a wise person choosing a looooooooong way to reach his destination. Hardwork always pays off. You went around and reached the other side of the lake.")
            elif decisions["lake_around_across"] == "across":
                print("Swimmer! Unfortunately, you were caught into a deadly battle with a crocodile! Your health is halved.")
                health -= 10

            decisions["lake_river_house"] = input("You notice a house and a river. Which do you go to (river/house)? ").lower()
            if decisions["lake_river_house"] == "house":
                print("You go to the house and are greeted by a beautiful mistress... She doesn't like the way you behave and you lose 5 health points.")
                health -= 10

                if health <= 0:
                    print("You now have 0 health points and you lost the game...")
                else:
                    print("You have survived ... You win!")
            if decisions["lake_river_house"] == "river":
                decisions["river_ride_boat"] = input("Would you like to take boat ride in river (yes/no)? ").lower()
                if decisions["river_ride_boat"] == "yes":
                    print("Ohhh water entered into boat!")
                    print("Alas!!!  You Lost!")
                else:
                    print("Mad you can't cross river without boat, You lost!!!")
            else:
                print("You lost dummy. This is not even a choiceee!!")
        else:
            print("You fell down into a well, blind person! You lost")

    else:
        print("Well, see ya soon!")
    
else:
    print("You're not old enough. SORRY :(")
