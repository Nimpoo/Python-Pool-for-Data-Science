from S1E9 import Character


class Baratheon(Character):

    """Representing the Baratheon family."""

    def __init__(self, first_name):

        """Init info's Baratheon"""

        self.is_alive = True
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):

        return (f"Vector {self.family_name, self.eyes, self.hairs}")

    def __repr__(self):

        return (f"Vector {self.family_name, self.eyes, self.hairs}")

    def die(self):

        """Method for Baratheon to die"""

        self.is_alive = False


class Lannister(Character):

    """
    Class 'character' for Lannister
    """

    def __init__(self, first_name, is_alive=True):

        """Init info's Lannister"""

        self.is_alive = is_alive
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):

        return (f"Vector {self.family_name, self.eyes, self.hairs}")

    def __repr__(self):

        return (f"Vector {self.family_name, self.eyes, self.hairs}")

    def die(self):

        """Method for Lannister to die"""

        self.is_alive = False

    @staticmethod
    def create_lannister(first_name, bool):

        """Creat Lannister"""

        c = Lannister(first_name, bool)
        return (c)
