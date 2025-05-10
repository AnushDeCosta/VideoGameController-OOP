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


# Test code
character = Character("DeadPool")
character.jump()
character.dodge()
character.attack()
character.aim_bow()
character.shoot_arrow()
character.craft_arrow()
character.display_quiver()
