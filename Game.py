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

    def wants_to_play(self):
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
                    "Alright! Now you followed the path, exhausted, you walk and reach out to a lake. You quench your thirst. Do you swim across or go around? (across, around) ").lower()

                if ans == "around":
                    print(
                        "You are a wise person choosing a looooooooong way to reach his/her destination. Hardwork always pays off! You went around and reached the other side of the lake.")
                elif ans == "across":
                    print(
                        "Swimmer! Unfortunately, you were caught into a deadly battle with a crocodile! Your health bar has been halved :(")
                    health -= 10

                ans = input("You notice a house and a river. What would you choose? (river/house) ")
                if ans == "house":
                    print(
                        "You went to the house and was greeted by a beautiful mistress. She didn't like your behaviour and thus deducted 5 points from your health level bar!")
                    health -= 5

                    if health <= 0:
                        print("Your health bar is empty now, cannot continue :(")
                        print("Better luck next time!")
                    else:
                        print("HURAYY!")
                        print("You have survived. VICTORY!")

                elif ans == "river":
                    ride = input("Would you like to take boat ride in river (yes/no)? ")
                    if ride == "yes":
                        print("Ohhh water entered into boat!")
                        print("Alas!!!  You Lost!")
                    else:
                        print("Mad you can't cross river without boat, You lost!!!")

                else:
                    print("You lost dummy. This is not even a choice!")
            else:
                print("You fell down into a well, blind person! You lost.")

        else:
            print("Well, see you soon!")

# uncomment to play the game 
'''
user = Game()
if user.check_age(18):
    user.wants_to_play()
'''

