from character import Character
from button import Button
from trigger import Trigger


class Controller:
    """
    Represents a game controller composed of triggers, action buttons,
    and directional buttons. Aggregates a Character instance.
    """

    # TODO: Add joystick support (optional challenge)

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

    def map_controller(self):
        """
        Creates and maps all buttons to the controller's internal lists.
        """
        # Action buttons: A, B, X, Y
        self.__action_buttons.append(Button("A"))  # jump
        self.__action_buttons.append(Button("B"))  # dodge
        self.__action_buttons.append(Button("X"))  # craft_arrow
        self.__action_buttons.append(Button("Y"))  # attack

        # Trigger buttons: LT, RT
        self.__triggers.append(Trigger("LT"))  # aim_bow
        self.__triggers.append(Trigger("RT"))  # shoot_arrow

        # Directional buttons: ↑, ↓, ←, →
        self.__directional_buttons.append(Button("↑"))
        self.__directional_buttons.append(Button("↓"))
        self.__directional_buttons.append(Button("←"))
        self.__directional_buttons.append(Button("→"))

    def set_character(self, character: Character):
        """
        Updates the controller's character.
        :param character: Character to control.
        """
        self.__character = character

    def press_button(self, button: Button):
        """
        Simulates pressing a button on the controller.
        :param button: The Button object to be pressed.
        :return: None
        """
        button.on_press(self.__character)
