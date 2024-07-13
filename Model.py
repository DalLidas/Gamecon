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

class enemy:
    def __init__(self, point: Point, id: str, type: str, hp: int, attack: int, direction: str, speed: int, waitTurns: int):
        self.point = point
        self.id = id
        self.type = type
        self.hp = hp
        self.attack = attack
        self.direction = direction
        self.speed = speed
        self.waitTurns = waitTurns

class Model:
    enemy = []
    worldMap = [[]]

    def __init__(self):
        pass

    def Run(self, unitResponse, worldResponse):
        


        return {}


    def checkTheMostDanger(self, zombies):

        if len(zombies) <= 1:
            return AttackTargetOrder(Point(zombies[0].x, zombies[0].y), zombies[0].blockId)
        else:

            zombies.sort(key=lambda x: x.waitTurns, reverse=True)

            for zombie in zombies:
                if zombie.type == "bomber":
                    return AttackTargetOrder(Point(zombie.x, zombie.y), zombie.blockId)

                elif zombie.type == "liner":
                    return AttackTargetOrder(Point(zombie.x, zombie.y), zombie.blockId)

                elif zombie.type == "juggernaut":
                    return AttackTargetOrder(Point(zombie.x, zombie.y), zombie.blockId)

                elif zombie.type == "chaos_knight":
                    return AttackTargetOrder(Point(zombie.x, zombie.y), zombie.blockId)

                elif zombie.type == "fast":
                    return AttackTargetOrder(Point(zombie.x, zombie.y), zombie.blockId)

                else:
                    return AttackTargetOrder(Point(zombie.x, zombie.y), zombie.blockId)

