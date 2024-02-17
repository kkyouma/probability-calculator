import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents.extend([color] * quantity)

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
    count_success = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {color: drawn_balls.count(color) for color in set(drawn_balls)}

        success = True
        for color, quantity in expected_balls.items():
            if drawn_dict.get(color, 0) < quantity:
                success = False
                break

        if success:
            count_success += 1

    return count_success / num_experiments
