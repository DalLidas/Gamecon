class Strategies:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def first_strategy(self):
        move_request_map = {
            {"x": self.x + 2,
             "y": self.y},

            {"x": self.x + 2,
             "y": self.y - 1},

            {"x": self.x,
             "y": self.y - 1},

            {"x": self.x + 1,
             "y": self.y + 1},

            {"x": self.x - 1,
             "y": self.y},

            {"x": self.x - 1,
             "y": self.y},

            {"x": self.x,
             "y": self.y + 1},

            {"x": self.x - 1,
             "y": self.y - 1},

            {"x": self.x,
             "y": self.y - 2},

            {"x": self.x + 1,
             "y": self.y - 2}
        }
        return move_request_map
