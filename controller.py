from character import Character


class Controller:
    """
    Represents a game controller composed of triggers, action buttons,
    and directional buttons. Aggregates a Character instance.
    TODO: Add joystick support (optional challenge).
    """

    def __init__(self, character: Character):
        """
        Initializes the controller with empty button lists and a character.
        :param character: Character object to be controlled.
        """
        self.__triggers = []
        self.__action_buttons = []
        self.__directional_buttons = []
        self.__character = character

    def get_triggers(self):
        """
        Returns the list of trigger buttons.
        """
        return self.__triggers

    def get_action_buttons(self):
        """
        Returns the list of action buttons.
        """
        return self.__action_buttons

    def get_directional_buttons(self):
        """
        Returns the list of directional buttons.
        """
        return self.__directional_buttons

    def set_character(self, character: Character):
        """
        Updates the controller's character.
        :param character: Character to control.
        """
        self.__character = character

    def press_button(self):
        """
        Placeholder method for button press logic.
        """
        pass
