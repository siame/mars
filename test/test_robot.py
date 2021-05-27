import pytest
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
