#!/usr/bin/env python3

class Love:

    ALLOWED_TYPES = {
        'agape',
        'phileo',
        'eros',
        'anal',
    }

    def __init__(self, type):
        if type not in self.ALLOWED_TYPES:
            raise LoveError(f"This is not love: {type}")
        self.type = type

    def __repr__(self):
        return f"{self.__class__.__name__}({self.type})"

    @classmethod
    def sample(cls):
        """ A random love constructor """
        type = random.choice(cls.ALLOWED_TYPES)
        return cls(type)


class Loves(list):

    def __lt__(self, other):
        return set(self) < set(other)

    def __gt__(self, other):
        return set(self) > set(other)


class Person:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"I'm a person, I'm too complicated to be summarized by a repr."


class Relationship:

    def __init__(self, romeo, juliet, loves):
        self.romeo = romeo
        self.juliet = juliet
        self.loves = loves


agape   = Love('agape')
phileo  = Love('phileo')
eros    = Love('eros')
anal    = Love('anal')

friends = Loves([phileo])
besties = Loves([agape, phileo])
lust    = Loves([eros, anal])
perfect = Loves([agape, phileo, eros, anal])

j = Person('jing')
J = Person('jason')

this = Relationship(
    J,
    j,
    perfect
)


