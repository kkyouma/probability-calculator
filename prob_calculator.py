import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.balls.extend([color] * quantity)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls += self.contents
            self.contents = []
        else:
            drawn_balls += random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
