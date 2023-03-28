import random
import string

from dataclasses import dataclass, field


def generate_id() -> str:

    """
    generator random
    """

    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:

    """
    stud class
    """

    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=True, default=True)
    id: str = field(init=False)
    login: str = field(init=False)

    def __post_init__(self):

        """
        post init function
        """

        self.id = generate_id()
        self.login = self.name[0].upper() + self.surname[:8].lower()
