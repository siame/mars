from collections import namedtuple
from enum import Enum

from toolz import partition_all

Position = namedtuple('Position', ('x', 'y'))


class FallOffEdgeException(Exception):
    pass


class UnknownInstructionException(Exception):
    pass


class Orientation(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


class Grid:
    def __init__(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.lost_robots = set()


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
            return f'{robot.x} {robot.y} {robot.orientation.name} LOST'
        else:
            return f'{robot.x} {robot.y} {robot.orientation.name}'


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
        lines = list(filter(None, map(str.strip, lines)))

    grid_line = lines[0]
    grid_coords = map(int, grid_line.split(' '))

    grid = Grid(*grid_coords)

    for robot_line, instruction_line in partition_all(2, lines[1:]):
        robot_line = robot_line.split(' ')
        robot = Robot(int(robot_line[0]), int(robot_line[1]), robot_line[2],
                      grid)

        for instruction in instruction_line:
            if instruction == 'F':
                try:
                    robot.move_forward()
                except FallOffEdgeException:
                    break

            elif instruction == 'R':
                robot.rotate_clockwise()
            elif instruction == 'L':
                robot.rotate_anticlockwise()
            else:
                raise UnknownInstructionException()

        print(robot)
