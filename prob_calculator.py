import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.balls = []
        for color, quantity in kwargs.items():
            self.balls.extend([color] * quantity)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
