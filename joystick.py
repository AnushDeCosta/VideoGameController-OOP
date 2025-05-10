from button import Button


class Joystick(Button):
    """
    Represents a joystick input. Inherits from Button.
    Can control character movement or rotation.
    """

    def on_press(self, character):
        """
        Triggers character movement or rotation based on the joystick mapping.
        :param character: The character object to control.
        """
        if self.get_mapping() == "LJ":
            character.move_up()
            character.move_right()
        elif self.get_mapping() == "RJ":
            character.rotate(45)
