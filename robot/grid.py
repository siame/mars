__all__ = ['Grid']


class Grid:
    def __init__(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.lost_robots = set()
