import random
from dataclasses import dataclass
from typing import List, Tuple


TYPES: List[str] = ["A", "B"]


class Model:
    def __init__(self,
                 width: int,
                 height: int,
                 density: float,
                 ratio: float):
        self.width = width
        self.height = height
        self.size = width * height
        self.density = density
        self.agents = [Agent(random.choice((width)),
                             random.choice((height)),
                             random.choice[TYPES]) for _ in self.size]

    def equilibrium(self):
        pass

    def step(self):
        pass

    def reset(self):
        pass

    def run(self):
        pass


@dataclass
class Agent:
    group: str = None
    _position: Tuple[int, int] = (None, None)
    _satisfied: bool = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = tuple(value)

    @property
    def is_satisfied(self):
        return self._satified

    @is_satisfied.setter
    def is_satisfied(self):
        self._satisfied = not self._satified
