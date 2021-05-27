import pytest
from robot.grid import Grid, InvalidGridBoundsException


@pytest.mark.parametrize('x_limit,y_limit', [(1, 1), (1, 2), (2, 1)])
def test_grid_correct_limits(x_limit, y_limit):
    Grid(x_limit, y_limit)


@pytest.mark.parametrize('x_limit,y_limit', [(0, 0), (-1, 1), (1, -1)])
def test_grid_incorrect_limits(x_limit, y_limit):
    with pytest.raises(InvalidGridBoundsException):
        Grid(x_limit, y_limit)
