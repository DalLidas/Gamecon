from DataClasses import *


class Model:
    def __init__(self):
        self.enemy = []
        self.worldMap = []

        self.BorderBaseCeil = []
        self.buildPlan = []

    def Run(self, unitResponse, worldResponse):
        return {"attack": self.attack(unitResponse, worldResponse), "build": self.build(unitResponse, worldResponse),
                "moveBase": self.moveHead(unitResponse, worldResponse)}

    def attack(self, unitResponse, worldResponse):
        return self.checkTheMostDanger(unitResponse)

    def checkTheMostDanger(self, unitResponse):
        head = unitResponse["base"]["id"]
        zombies = unitResponse["zombies"]
        if len(zombies) <= 1:
            return AttackTargetOrder(Point(zombies[0].x, zombies[0].y), head)
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

    def newBuildPlan(self, unitResponse, worldResponse):
        ceils = unitResponse["base"]
        for ceil1 in ceils:
            for ceil2 in ceils:
                # Проверка сверху
                if int(ceil1["x"]) != int(ceil2["x"]) and int(ceil1["y"] + 1) != int(ceil2["y"]):
                    self.buildPlan.append(ceil1)

                # Проверка снизу
                if int(ceil1["x"]) != int(ceil2["x"]) and int(ceil1["y"] - 1) != int(ceil2["y"]):
                    self.buildPlan.append(ceil1)

                # Проверка справа
                if int(ceil1["x"] + 1) != int(ceil2["x"]) and int(ceil1["y"]) != int(ceil2["y"]):
                    self.buildPlan.append(ceil1)

                # Проверка слева
                if int(ceil1["x"] - 1) != int(ceil2["x"]) and int(ceil1["y"]) != int(ceil2["y"]):
                    self.buildPlan.append(ceil1)

        self.BorderBaseCeil

    def build(self, unitResponse, worldResponse):
        player = Player(unitResponse["player"])
        builds = []

        if len(self.buildPlan) == 0:
            self.newBuildPlan(unitResponse, worldResponse)

        if player.gold > len(self.buildPlan):
            self.newBuildPlan(unitResponse, worldResponse)

        for _ in range(player.gold):
            builds.append(self.buildPlan.pop)

        return builds

    def moveHead(self, unitResponse, worldResponse):
        # move head of the base
        pass
