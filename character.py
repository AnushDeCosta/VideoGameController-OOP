class Character:
    """
    Represents a game character with a name, a number of arrows,
    and a jumping state.
    """

    def __init__(self, name):
        """
        Initializes the character with a name, a default arrow count of 6,
        and sets jumping status to False.
        :param name: str - The name of the character
        """
        self.__name = name
        self.__arrows = 6
        self.__is_jumping = False

    def get_name(self):
        """
        Returns the name of the character.
        :return: str
        """
        return self.__name

    def get_arrows(self):
        """
        Returns the current number of arrows the character has.
        :return: int
        """
        return self.__arrows

    def get_is_jumping(self):
        """
        Returns a string representation of the character's jumping state.
        :return: str - "Jumping" or "Not Jumping"
        """
        if self.__is_jumping == False:
            return "Not Jumping"
        else:
            return "Jumping"

    def jump(self):
        """
        Makes the character jump by updating their jumping status and
        displaying a message.
        :return: None, Prints a message
        """
        self.__is_jumping = True
        print(f"{self.__name} jumps in the air")

    def dodge(self):
        """
        Displays a message indicating the character has dodged an attack.
        :return: None
        """
        print(f"{self.__name} swiftly evades the enemy.")

    def aim_bow(self):
        """

        :return:
        """
        pass

    def shoot_arrow(self):
        """

        :return:
        """
        pass

    def craft_arrow(self):
        """

        :return:
        """
        pass

    def display_quiver(self):
        """

        :return:
        """
        pass

# Test code
character = Character("Thomas")
character.jump()
character.dodge()
