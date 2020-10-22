from info import PlayerInfo

health = 20

class Game:

    def check_age(self, age):
        """
        This method checks the user entered age is more than 16.i.e. check player is eligible to play this game
        :return:
        boolean value i.e. age is greater then true and vice versa.
        """
        if age >= 16:
            print("You're old enough to play!")
            return True
        else:
            print("You're not old enough. SORRY :(")
            return False

    def wants_to_play(self,):
        """
        Real fun begins here...
        :return:
        Nothing
        """
        global health
        play = input("Do you want to play? (yes/no) ").lower()
        if play == "yes":
            print("Wohoo! Let's play!")
            choice1 = input("Would you like to take a Left turn or a Right turn? (left/right) ").lower()
            if choice1 == "left":
                ans = input(
                    "Alright! Now you followed a path downhill, exhausted, you reached down to a lake. You quench your thirst. Do you swim across or go around the lake? (across, around) ").lower()
                if ans == "around":
                    print(
                        "You are a wise person choosing a looooooooong way to reach his/her destination. Hardwork always pays off! You walked around to the other side of the lake.")
                elif ans == "across":
                    print(
                        "Swimmer! Unfortunately, you were caught in a deadly battle with a crocodile! Your health bar has been halved :(")
                    health -= 10
                    print("You have %s life remaining" % health)
                else:
                    print('Invalid option. Please try to type carefully!')

                    ans = input("You notice a house and a car. What would you choose? (house/car) ").lower()
                    if ans == "house":
                        print("You went to the house and was greeted by a beautiful mistress. She didn't like your behaviour and thus deducted 5 points from your health level bar!")
                        health -= 5
                        print('You have %s life remaining' % health)
                        ans = input("There are only two ways to escape the mistress. Outside or down the stairs to the dungeon. Where would you go? (outside/dungeon)").lower()
                        if ans == "dungeon":
                            print("Aren't you the brave type :) WELCOME TO THE DUNGEON! See you at Dungeon 2.0")
                        elif ans == "outside":
                            print("You can't get to the car this time, cause you get eaten by a beast!!!")
                        else:
                            print('Invalid option. Please try to type carefully!')

                    # This statement is not really needed in this  version of the game.
                    # if health <= 0:
                    #     print("Your health bar is empty now, cannot continue :(")
                    #     print("Better luck next time!")
                    # else:
                    #     print("HURAYY!")
                    #     print("You have survived. VICTORY!")

                    elif ans == "car":
                        ride = input("Would you like to go for a ride with the car (yes/no)? ")
                        if ride == "yes":
                            print("Ohhh You can't drive!")
                            print("You crashed!!!  You Lost!!!")
                        elif ride == 'no':
                            print("Mad you can't sit there all night, there are creatures lurking everywhere! You lost!!!")
                        else:
                            print('Invalid option. Please try to type carefully!')

                    else:
                        print("You lost dummy. This is not even a choice!")
            elif choice1 == "right":
                print("Right is not always the best choice! You fell down into a well, blind person! You lost.")

            else:
                print('Invalid option. Please try to type carefully!')

        elif play == 'no':
            print("Well, see you soon!")
        else:
            print('Invalid option. Please try to type carefully!')

# uncomment to play the game 




