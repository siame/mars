from robot.grid import Grid
from robot.robot import Orientation, Position, Robot


def test_mission():
    grid = Grid(5, 3)

    robot_one = Robot(1, 1, 'E', grid)
    robot_one.process_instruction_line('RFRFRFRF')

    assert robot_one.position.x == 1
    assert robot_one.position.y == 1
    assert robot_one.orientation == Orientation.E
    assert robot_one.lost is False

    assert len(grid.lost_robots) == 0

    robot_two = Robot(3, 2, 'N', grid)
    robot_two.process_instruction_line('FRRFLLFFRRFLL')

    assert robot_two.position.x == 3
    assert robot_two.position.y == 3
    assert robot_two.orientation == Orientation.N
    assert robot_two.lost is True

    assert len(grid.lost_robots) == 1
    assert Position(3, 4) in grid.lost_robots

    robot_three = Robot(0, 3, 'W', grid)
    robot_three.process_instruction_line('LLFFFLFLFL')

    assert robot_three.position.x == 2
    assert robot_three.position.y == 3
    assert robot_three.orientation == Orientation.S
    assert robot_three.lost is False

    assert len(grid.lost_robots) == 1
