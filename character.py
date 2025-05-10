class Character:
    """
    Represents a game character with a name, arrow count, and jumping state.
    """

    def __init__(self, name):
        """
        Initializes the character with a name, 6 arrows, and not jumping.
        """
        self.__name = name
        self.__arrows = 6
        self.__is_jumping = False
        self.__x = 0
        self.__y = 0
        self.__facing_angle = 0

    def get_name(self):
        """
        Returns the character's name.
        """
        return self.__name

    def get_arrows(self):
        """
        Returns the number of arrows the character has.
        """
        return self.__arrows

    def get_is_jumping(self):
        """
        Returns the jumping state as a readable string.
        """
        return "Jumping" if self.__is_jumping else "Not Jumping"

    def jump(self):
        """
        Makes the character jump and updates the jumping state.
        """
        self.__is_jumping = True
        print(f"{self.__name} jumps in the air.")

    def dodge(self):
        """
        Displays a message indicating the character dodged an attack.
        """
        print(f"{self.__name} swiftly evades the enemy.")

    def attack(self):
        """
        Displays a message indicating the character has attacked a foe.
        """
        print(f"{self.__name} strikes the foe.")

    def aim_bow(self):
        """
        Displays a message indicating the character is aiming.
        """
        print(f"{self.__name} takes aim.")

    def shoot_arrow(self):
        """
        Reduces the arrow count and displays a shooting message.
        """
        self.__arrows -= 1
        print(f"{self.__name} releases the shot.")
        print(f"{self.__name} has {self.__arrows} arrow(s) left.")

    def craft_arrow(self):
        """
        Increases the arrow count and displays a crafting message.
        """
        self.__arrows += 1
        print(f"{self.__name} crafts a new arrow.")
        print(f"{self.__name} now has {self.__arrows} arrow(s).")

    def display_quiver(self):
        """
        Displays the number of arrows currently in the quiver.
        """
        print(f"There are {self.__arrows} arrows remaining in the quiver.")

    def move_up(self):
        self.__y += 1
        print(f"{self.__name} moves up to position ({self.__x}, {self.__y}).")

    def move_down(self):
        self.__y -= 1
        print(f"{self.__name} moves down to position ({self.__x}, {self.__y}).")

    def move_left(self):
        self.__x -= 1
        print(f"{self.__name} moves left to position ({self.__x}, {self.__y}).")

    def move_right(self):
        self.__x += 1
        print(f"{self.__name} moves right to position ({self.__x}, {self.__y}).")

    def rotate(self, degrees):
        self.__facing_angle = (self.__facing_angle + degrees) % 360
        print(f"{self.__name} rotates to {self.__facing_angle}° facing.")
