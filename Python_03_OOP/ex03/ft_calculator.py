class calculator:

    """
    Calculator class
    """

    def __init__(self, list):

        """Init list"""

        self.list = list

    def __add__(self, object) -> None:

        """Addition"""

        self.list = [i + object for i in self.list]
        print(self.list)

    def __mul__(self, object) -> None:

        """Multiplication"""

        self.list = [i * object for i in self.list]
        print(self.list)

    def __sub__(self, object) -> None:

        """Substraction"""

        self.list = [i - object for i in self.list]
        print(self.list)

    def __truediv__(self, object) -> None:

        """Division"""

        try:
            self.list = [i / object for i in self.list]
        except Exception as e:
            print(e)
            exit()
        print(self.list)
