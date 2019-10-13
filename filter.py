from helpers.filter_math_helper import FilterMath


class Filter:

    def __init__(self, window, func):
        self.window = window
        self.points = []
        self.stack = []
        self.func = func

    def filter(self, points_arr):

        for item in points_arr:

            self.stack.append(item)
            self.points.append(self.func(self.stack))

            if len(self.stack) == self.window:
                self.stack.pop(0)

        return self.points



