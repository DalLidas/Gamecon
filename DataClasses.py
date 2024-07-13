from dataclasses import dataclass
from typing import Any
from typing import List


@dataclass
class Zombie:
    attack: int
    direction: str
    health: int
    id: str
    speed: int
    type: str
    waitTurns: int
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'Zombie':
        _attack = int(obj.get("attack"))
        _direction = str(obj.get("direction"))
        _health = int(obj.get("health"))
        _id = str(obj.get("id"))
        _speed = int(obj.get("speed"))
        _type = str(obj.get("type"))
        _waitTurns = int(obj.get("waitTurns"))
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        return Zombie(_attack, _direction, _health, _id, _speed, _type, _waitTurns, _x, _y)

    def __iter__(self):
        for value in self.__dict__.values():
            yield value


@dataclass
class LastAttack:
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'LastAttack':
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        return LastAttack(_x, _y)


@dataclass
class Base:
    attack: int
    health: int
    id: str
    isHead: bool
    lastAttack: LastAttack
    range: int
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'Base':
        _attack = int(obj.get("attack")) if obj.get("attack") is not None else 0
        _health = int(obj.get("health"))
        _id = str(obj.get("id"))
        _isHead = bool(obj.get("isHead"))
        _lastAttack = LastAttack.from_dict(obj.get("lastAttack"))
        _range = int(obj.get("range"))
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        return Base(_attack, _health, _id, _isHead, _lastAttack, _range, _x, _y)

    def __iter__(self):
        for value in self.__dict__.values():
            yield value


@dataclass
class EnemyBlock:
    attack: int
    health: int
    isHead: bool
    lastAttack: LastAttack
    name: str
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'EnemyBlock':
        _attack = int(obj.get("attack"))
        _health = int(obj.get("health"))
        _isHead = bool(obj.get("isHead"))
        _lastAttack = LastAttack.from_dict(obj.get("lastAttack"))
        _name = str(obj.get("name"))
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        return EnemyBlock(_attack, _health, _isHead, _lastAttack, _name, _x, _y)

    def __iter__(self):
        for value in self.__dict__.values():
            yield value


@dataclass
class Player:
    enemyBlockKills: int
    gameEndedAt: str
    gold: int
    name: str
    points: int
    zombieKills: int

    @staticmethod
    def from_dict(obj: Any) -> 'Player':
        _enemyBlockKills = int(obj.get("enemyBlockKills"))
        _gameEndedAt = str(obj.get("gameEndedAt"))
        _gold = int(obj.get("gold"))
        _name = str(obj.get("name"))
        _points = int(obj.get("points"))
        _zombieKills = int(obj.get("zombieKills"))
        return Player(_enemyBlockKills, _gameEndedAt, _gold, _name, _points, _zombieKills)

    def __iter__(self):
        for value in self.__dict__.values():
            yield value


@dataclass
class Units:
    base: List[Base]
    enemyBlocks: List[EnemyBlock]
    player: Player
    realmName: str
    turn: int
    turnEndsInMs: int
    zombies: List[Zombie]

    @staticmethod
    def from_dict(obj: Any) -> 'Units':
        _base = [Base.from_dict(y) for y in obj.get("base")]
        _enemyBlocks = [EnemyBlock.from_dict(y) for y in obj.get("enemyBlocks")]
        _player = Player.from_dict(obj.get("player"))
        _realmName = str(obj.get("realmName"))
        _turn = int(obj.get("turn"))
        _turnEndsInMs = int(obj.get("turnEndsInMs"))
        _zombies = [Zombie.from_dict(y) for y in obj.get("zombies")]
        return Units(_base, _enemyBlocks, _player, _realmName, _turn, _turnEndsInMs, _zombies)

    def __iter__(self):
        for value in self.__dict__.values():
            yield value


@dataclass
class Zpot:
    x: int
    y: int
    type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Zpot':
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        _type = str(obj.get("type"))
        return Zpot(_x, _y, _type)

    def __iter__(self):
        for value in self.__dict__.values():
            yield value


@dataclass
class World:
    realmName: str
    zpots: List[Zpot]

    @staticmethod
    def from_dict(obj: Any) -> 'World':
        _realmName = str(obj.get("realmName"))
        _zpots = [Zpot.from_dict(y) for y in obj.get("zpots")]
        return World(_realmName, _zpots)

    def __iter__(self):
        for value in self.__dict__.values():
            yield value
