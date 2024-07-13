from DataClasses import *

class Model:
    enemy = []
    worldMap = [[]]

    def __init__(self):
        pass

    def Run(self, unitResponse, worldResponse):
        return {"attack": self.attack(), "build": self.build(), "moveBase": self.moveHead()}

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
                
    def attack():
        pass

    def build(self, player: Player, base: Base):
        for gold in range(player.gold):
            # build 1 cell for each gold
            pass

    def moveHead(self):
        # move head of the base
        pass
