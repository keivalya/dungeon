print("DUNGEON GAME! Make your choices, well")

name = input("Hey! What's yout name? ")
age = input("How old are you? ")

while (not age.isnumeric()) or int(age) < 0:
    age = input("That age doesn't seem right.\nCan you enter you current age?")

age = int(age)

print("Namaste", name, "so you're", age, "huh!")

health = 20

inventory = []

if age >= 16:
    print("You're old enough to play!")

    print("You are starting with", health, "health")

    wants2play = input("Do you want to play? ").lower()
    if wants2play == "yes":
        print("Let's PLAY!")
        lor = input("First choice... Left or Right (left/right)?").lower()
        if lor == "left":
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

            elif ans == "river":
                print("You walk to the river and discover a short man eating alone by a fire.")
                greet_or_fight = input("Do you greet him or try to fight him for his food? (greet/fight)").lower()
                if greet_or_fight == "greet":
                    print("After taking a moment to look at you, the man decides that you are of no harm")
                    print("He decides to share some of his food with you.")
                    if health < 20:
                        print("You enjoy a nice conversation with eating. You feel better after the delicious meal.")
                        # TODO Decide if health should be cappedat 20. If not, just heal the specified amount
                        if health > 15:
                            health = 20
                        else:
                            health += 5
                    else:
                        print("You don't feel healthier, but you enjoyed a nice conversation while eating the delicious meal.")
                elif greet_or_fight == "fight":
                    print("You charge at the man and tackle him down to the ground. He takes out a knife and slashes you near your gut.")
                    health -= 15
                    if health <= 0:
                        print("You died over a meal that you didn't even get to taste. Was it worth it?")
                    else:
                        print("You survive the first slash and manage wrestle the knife out of his hand.")
                        print("You leap for the knife and threaten to harm your opponent if he doesn't give you his entire meal. He yields and allows you toleave with his knife and the meal.")
                        print("You recover a large amount of health after eating the entire meal.")
                        # TODO Change if health shouldn't be capped at 20
                        if health < 3:
                            health += 17
                        else:
                            health = 20
                        print("You now have a knife in your inventory")
                        inventory.append("knife")
                        print("You survived so far, but are you proud of what you have done?")
            else:
                print("You couldn't make up you mind, so you stood still until you starved to death")
        else:
            print("You fell down into a well, blind person! You lost")

    else:
        print("Well, see ya soon!")

else:
    print("You're not old enough. SORRY :(")
