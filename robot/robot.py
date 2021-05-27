from collections import namedtuple
from enum import Enum

from .exceptions import (FallOffEdgeException, OutOfBoundsException,
                         UnknownInstructionException)

__all__ = ['Robot', 'Orientation']

Position = namedtuple('Position', ('x', 'y'))


class Orientation(Enum):
    N = 0
    E = 90
    S = 180
    W = 270


class Robot:
    def __init__(self, x, y, orientation, grid):
        if x < 0 or y < 0:
            raise OutOfBoundsException()

        self.position = Position(x, y)
        self.orientation = Orientation.__members__[orientation]

        if self.position.x > grid.x_limit or self.position.y > grid.y_limit:
            raise OutOfBoundsException()

        self.grid = grid
        self.lost = False

    def rotate_clockwise(self):
        new_orientation = self.orientation.value + 90
        self.orientation = Orientation(new_orientation % 360)

    def rotate_anticlockwise(self):
        new_orientation = self.orientation.value - 90
        self.orientation = Orientation(new_orientation % 360)

    def move_forward(self):
        if self.orientation == Orientation.N:
            new_position = Position(self.position.x, self.position.y + 1)
        elif self.orientation == Orientation.E:
            new_position = Position(self.position.x + 1, self.position.y)
        elif self.orientation == Orientation.S:
            new_position = Position(self.position.x, self.position.y - 1)
        elif self.orientation == Orientation.W:
            new_position = Position(self.position.x - 1, self.position.y)

        if new_position in self.grid.lost_robots:
            return

        if (new_position.x < 0 or new_position.y < 0
                or new_position.x > self.grid.x_limit
                or new_position.y > self.grid.y_limit):
            self.grid.lost_robots.add(new_position)
            self.lost = True

            raise FallOffEdgeException()

        self.position = new_position

    def process_instruction_line(self, instruction_line):
        for instruction in instruction_line:
            if instruction == 'F':
                try:
                    self.move_forward()
                except FallOffEdgeException:
                    break

            elif instruction == 'R':
                self.rotate_clockwise()
            elif instruction == 'L':
                self.rotate_anticlockwise()
            else:
                raise UnknownInstructionException()

    def __repr__(self):
        if self.lost:
            return f'{self.position.x} {self.position.y} {self.orientation.name} LOST'  # noqa
        else:
            return f'{self.position.x} {self.position.y} {self.orientation.name}'  # noqa
