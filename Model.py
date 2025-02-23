from DataClasses import *


class Model:
    def __init__(self):
        self.enemy = []
        self.worldMap = []

        self.lockedPaces = []
        # self.BorderBaseCeil = []
        self.buildPlan = []

    def Run(self, unitResponse, worldResponse):
        attak = self.attack(unitResponse, worldResponse)
        build = self.build(unitResponse, worldResponse)
        move = self.moveHead(unitResponse, worldResponse)

        return {"attack": attak, "build": build, "moveBase": move}

    def attack(self, unitResponse, worldResponse):
        return self.checkTheMostDanger(unitResponse)

    def checkTheMostDanger(self, unitResponse):
        if "base" in unitResponse and unitResponse["base"] is not None:
            cells = [Base.from_dict(y) for y in unitResponse["base"]]
            zombies = [Zombie.from_dict(y) for y in unitResponse["zombies"]]
            zombies.sort(key=lambda x: x.waitTurns, reverse=True)

            attackList = []

            for cell in cells:
                for zombie in zombies:
                    if pow(pow(zombie.x - cell.x, 2) + pow(zombie.y - cell.y, 2), 0.5):
                        if zombie.type == "bomber":
                            attackList.append(AttackTargetOrder(Point(zombie.x, zombie.y), cell.id))

                        elif zombie.type == "liner":
                            attackList.append(AttackTargetOrder(Point(zombie.x, zombie.y), cell.id))

                        elif zombie.type == "juggernaut":
                            attackList.append(AttackTargetOrder(Point(zombie.x, zombie.y), cell.id))

                        elif zombie.type == "chaos_knight":
                            attackList.append(AttackTargetOrder(Point(zombie.x, zombie.y), cell.id))

                        elif zombie.type == "fast":
                            attackList.append(AttackTargetOrder(Point(zombie.x, zombie.y), cell.id))

                        else:
                            attackList.append(AttackTargetOrder(Point(zombie.x, zombie.y), cell.id))
            return attackList

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
                if pUp.x != int(ceil2["x"]) and pUp.y != int(ceil2["y"]) and pUp not in self.lockedPaces:
                    self.buildPlan.append(pUp)

                # Проверка снизу
                if pDown.x != int(ceil2["x"]) and pDown.y != int(ceil2["y"]) and pDown not in self.lockedPaces:
                    self.buildPlan.append(pDown)

                # Проверка справа
                if pRight.x != int(ceil2["x"]) and pRight.y != int(ceil2["y"]) and pRight not in self.lockedPaces:
                    self.buildPlan.append(pRight)

                # Проверка слева
                if pLeft.x != int(ceil2["x"]) and pLeft.y != int(ceil2["y"]) and pLeft not in self.lockedPaces:
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
