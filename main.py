from toolz import partition_all

from robot.grid import Grid
from robot.robot import Robot

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

        robot.process_instruction_line(instruction_line)

        print(robot)
