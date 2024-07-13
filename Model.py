from DataClasses import *


class Model:
    def __init__(self):
        self.enemy = []
        self.worldMap = []
        
        self.lockedPaces = []
        # self.BorderBaseCeil = []
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
        self.lockedPaces.clear()
        self.buildPlan.clear()

        wobjs = worldResponse["zpots"]
        for wobj in wobjs:
            self.lockedPaces.append(Point(int(wobj["x"]), int(wobj["y"] + 1)))
            self.lockedPaces.append(Point(int(wobj["x"]), int(wobj["y"] - 1)))
            self.lockedPaces.append(Point(int(wobj["x"] + 1), int(wobj["y"])))
            self.lockedPaces.append(Point(int(wobj["x"] - 1), int(wobj["y"])))

        ceils = unitResponse["base"]
        for ceil1 in ceils:
            for ceil2 in ceils:
                pUp = Point((ceil1["x"]), int(ceil1["y"] + 1))
                pDown = Point((ceil1["x"]), int(ceil1["y"] - 1))
                pRight = Point((ceil1["x"] + 1), int(ceil1["y"]))
                pLeft = Point((ceil1["x"] - 1), int(ceil1["y"]))

                # Проверка сверху
                if pUp.x != int(ceil2["x"]) and pUp.y != int(ceil2["y"]) and not pUp in self.lockedPaces:
                    self.buildPlan.append(pUp)

                # Проверка снизу
                if pDown.x != int(ceil2["x"]) and pDown.y != int(ceil2["y"]) and not pDown in self.lockedPaces:
                    self.buildPlan.append(pDown)

                # Проверка справа
                if pRight.x != int(ceil2["x"]) and pRight.y != int(ceil2["y"]) and not pRight in self.lockedPaces:
                    self.buildPlan.append(pRight)
                
                # Проверка слева
                if pLeft.x != int(ceil2["x"]) and pLeft.y != int(ceil2["y"]) and not pLeft in self.lockedPaces:
                    self.buildPlan.append(pLeft)

        
    def build(self, unitResponse, worldResponse):
        player = Player(unitResponse["player"])
        builds = []

        if len(self.buildPlan) == 0:
            self.newBuildPlan(unitResponse, worldResponse)

        if player.gold > len(self.buildPlan):
            self.newBuildPlan(unitResponse, worldResponse)

        for _ in range(player.gold):
            builds.append(self.buildPlan.pop().GetDict())
        
        return builds

    def moveHead(self, unitResponse, worldResponse):
        # move head of the base
        pass
