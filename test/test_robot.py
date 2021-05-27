import pytest
from robot.exceptions import OutOfBoundsException, UnknownInstructionException
from robot.grid import Grid
from robot.robot import Orientation, Position, Robot


@pytest.fixture
def grid():
    return Grid(3, 3)


@pytest.mark.parametrize('initial_orientation,rotated_orientation', [
    (Orientation.N, Orientation.E),
    (Orientation.E, Orientation.S),
    (Orientation.S, Orientation.W),
    (Orientation.W, Orientation.N),
])
def test_rotate_clockwise(initial_orientation, rotated_orientation, grid):
    robot = Robot(0, 0, initial_orientation.name, grid)

    robot.rotate_clockwise()

    assert robot.orientation == rotated_orientation


@pytest.mark.parametrize('initial_orientation,rotated_orientation', [
    (Orientation.N, Orientation.W),
    (Orientation.E, Orientation.N),
    (Orientation.S, Orientation.E),
    (Orientation.W, Orientation.S),
])
def test_rotate_anticlockwise(initial_orientation, rotated_orientation, grid):
    robot = Robot(0, 0, initial_orientation.name, grid)

    robot.rotate_anticlockwise()

    assert robot.orientation == rotated_orientation


@pytest.mark.parametrize('orientation,final_position', [
    (Orientation.N, Position(1, 2)),
    (Orientation.E, Position(2, 1)),
    (Orientation.S, Position(1, 0)),
    (Orientation.W, Position(0, 1)),
])
def test_move_forward(orientation, final_position, grid):
    robot = Robot(1, 1, orientation.name, grid)

    robot.move_forward()

    assert robot.position == final_position


def test_robot_process_instruction_line(grid):
    robot = Robot(1, 1, Orientation.E.name, grid)

    robot.process_instruction_line('RFLL')

    assert robot.position.x == 1
    assert robot.position.y == 0
    assert robot.orientation == Orientation.N
    assert robot.lost is False


def test_unknown_instruction(grid):
    robot = Robot(1, 1, Orientation.E.name, grid)

    with pytest.raises(UnknownInstructionException):
        robot.process_instruction_line('A')


@pytest.mark.parametrize('initial_position', [
    (Position(-1, 0)),
    (Position(0, -1)),
    (Position(3, 4)),
    (Position(4, 3)),
])
def test_robot_initialised_out_of_grid_bounds(initial_position, grid):
    with pytest.raises(OutOfBoundsException):
        Robot(initial_position.x, initial_position.y, Orientation.N.name, grid)
