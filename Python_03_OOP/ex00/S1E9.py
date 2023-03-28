from abc import ABC, abstractmethod


class Character(ABC):

    """
    Abstract class describe a character of GOT
    """

    def __init__(self, first_name):

        """Init the info's character"""

        self.first_name = first_name
        self.is_alive = True


    @abstractmethod
    def die(self):
        pass


class Stark(Character):

    """
    A subclass 'Character' from the Stark Family
    """

    def __init__(self, first_name, is_alive=True):

        """Init the info's character"""

        # self.first_name = first_name
        super().__init__(first_name)
        self.is_alive = is_alive

    def die(self):

        """Method to die"""

        self.is_alive = False
