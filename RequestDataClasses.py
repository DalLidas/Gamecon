from dataclasses import dataclass
from typing import Any
from typing import List


@dataclass
class Target:
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'Target':
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        return Target(_x, _y)


@dataclass
class Attack:
    blockId: str
    target: Target

    @staticmethod
    def from_dict(obj: Any) -> 'Attack':
        _blockId = str(obj.get("blockId"))
        _target = Target.from_dict(obj.get("target"))
        return Attack(_blockId, _target)


@dataclass
class Build:
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'Build':
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        return Build(_x, _y)


@dataclass
class MoveBase:
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'MoveBase':
        _x = int(obj.get("x"))
        _y = int(obj.get("y"))
        return MoveBase(_x, _y)


@dataclass
class Command:
    attack: List[Attack]
    build: List[Build]
    moveBase: MoveBase

    @staticmethod
    def from_dict(obj: Any) -> 'Command':
        _attack = [Attack.from_dict(y) for y in obj.get("attack")]
        _build = [Build.from_dict(y) for y in obj.get("build")]
        _moveBase = MoveBase.from_dict(obj.get("moveBase"))
        return Command(_attack, _build, _moveBase)
