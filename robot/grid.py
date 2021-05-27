__all__ = ['Grid', 'InvalidGridBoundsException']


class InvalidGridBoundsException(Exception):
    pass


class Grid:
    def __init__(self, x_limit, y_limit):
        if x_limit < 1 or y_limit < 1:
            raise InvalidGridBoundsException()

        self.x_limit = x_limit
        self.y_limit = y_limit
        self.lost_robots = set()
