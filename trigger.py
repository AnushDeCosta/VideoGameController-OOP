from button import Button


class Trigger(Button):
    """
    Represents a trigger button, inherited from Button.
    Can be extended with on_release() for held/released input logic.
    """

    def on_release(self):
        """
        Placeholder for future functionality when the trigger is released.
        """
        print(f"Trigger '{self.get_mapping()}' released.")
