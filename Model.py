class Point:
    x = 0
    y = 0
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def GetDict(self):
        return {"x": self.x, "y": self.y} 

def AttackTargetOrder(target: Point, blockId: str):
    return {"blockId": blockId, "target": target.GetDict()}

#TODO: что такое blockId? Вроде в канфе писали про то, что это имя нашей базы, но это как-то странно... Мнда...

class Model:
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
