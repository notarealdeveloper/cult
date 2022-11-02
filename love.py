#!/usr/bin/env python3

class Love:

    ALLOWED_TYPES = {'agape', 'phileo', 'eros', 'anal'}

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


