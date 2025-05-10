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

# Test code
character = Character("Thomas")
print(f"Your character's name is {character.get_name()}, You have {character.get_arrows()} arrows left and is {character.get_is_jumping()}")
