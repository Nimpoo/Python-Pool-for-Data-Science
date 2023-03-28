from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    """
    Representing the King.
    """

    def __init__(self, first_name):

        """Init info's King"""

        self.is_alive = True
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, eyes):

        """Set eyes"""

        self.eyes = eyes

    def set_hairs(self, hairs):

        """Set hairs"""

        self.hairs = hairs

    def get_eyes(self):

        """Return eyes"""

        return (self.eyes)

    def get_hairs(self):

        """Return hairs"""

        return (self.hairs)
