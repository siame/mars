from collections import namedtuple
from enum import Enum

from .exceptions import FallOffEdgeException

__all__ = ['Robot']

Position = namedtuple('Position', ('x', 'y'))


class Orientation(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


class Robot:
    def __init__(self, x, y, orientation, grid):
        self.x = x
        self.y = y
        self.orientation = Orientation.__members__[orientation]

        self.grid = grid
        self.lost = False

    def rotate_clockwise(self):
        new_orientation = self.orientation.value + 1
        self.orientation = Orientation(new_orientation % 4)

    def rotate_anticlockwise(self):
        new_orientation = self.orientation.value - 1
        self.orientation = Orientation(new_orientation % 4)

    def move_forward(self):
        if self.orientation == Orientation.N:
            new_position = Position(self.x, self.y + 1)
        elif self.orientation == Orientation.E:
            new_position = Position(self.x + 1, self.y)
        elif self.orientation == Orientation.S:
            new_position = Position(self.x, self.y - 1)
        elif self.orientation == Orientation.W:
            new_position = Position(self.x - 1, self.y)

        if new_position in self.grid.lost_robots:
            return

        if (new_position.x < 0 or new_position.y < 0
                or new_position.x > self.grid.x_limit
                or new_position.y > self.grid.y_limit):
            self.grid.lost_robots.add(new_position)
            self.lost = True

            raise FallOffEdgeException()

        self.x = new_position.x
        self.y = new_position.y

    def __repr__(self):
        if self.lost:
            return f'{self.x} {self.y} {self.orientation.name} LOST'
        else:
            return f'{self.x} {self.y} {self.orientation.name}'
