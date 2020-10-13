class PlayerInfo():

    def getInfo(self):
        """
        This method gets info from user in console.
        :return:
        age
        """
        name = input("Hey! What's your name? ")
        age = int(input("How old are you? "))
        print("Namaste", name, "so you're", age, "huh!")
        return age