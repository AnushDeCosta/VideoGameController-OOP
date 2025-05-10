from character import Character


class Button:
    """
    Represents a controller button and its input mapping.
    """

    def __init__(self, mapping):
        """
        Initializes the button with its mapping.
        """
        self.__mapping = mapping

    def get_mapping(self):
        """Returns the button's mapping."""
        return self.__mapping

    def on_press(self, character: Character):
        """
        Triggers a character action based on the button's mapping.
        :param character: Character object the button interacts with.
        :return: None
        """
        if self.__mapping == "A":
            character.jump()
        elif self.__mapping == "B":
            character.dodge()
        elif self.__mapping == "Y":
            character.attack()
        elif self.__mapping == "LT":
            character.aim_bow()
        elif self.__mapping == "RT":
            character.shoot_arrow()
        elif self.__mapping == "X":
            character.craft_arrow()
        elif self.__mapping == "LB":
            character.display_quiver()
