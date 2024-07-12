import requests # type: ignore
import json
from datetime import datetime

import logging

class Api:
    def __init__(self, serverURL, token, debug = False):
        self.serverURL = serverURL
        self.token = token

        # Форматирование времени в "часы:минуты:секунды"
        # current_time = datetime.now()
        # formatted_time = current_time.strftime("%H:%M:%S")

        # log = f"{formatted_time}:{method}: {msg}\n\n"

        # Настройка логгера
        logging.basicConfig(filename='app.log', 
                            level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

        self.headers = {
            "X-Auth-Token": f"{token}",
            "Content-Type": "application/json"
        }

    def Command(self, attacked, build, moveBase):
        data = json.JSONEncoder({"attack": attacked, "build": build, "moveBase": moveBase})
        response = requests.post(self.serverURL+ "/lay/zombidef/command", headers=self.headers, json=data)

        # Логирование
        logging.info(f"Command: {response._content}")
        print(f"Command: {response._content}")

        return response

        # Content type: application/json
        # {
        #     "attack": [
        #         {
        #         "blockId": "f47ac10b-58cc-0372-8562-0e02b2c3d479",
        #         "target": {
        #             "x": 1,
        #             "y": 1
        #             }
        #         }
        #     ],
        #     "build": [
        #         {
        #         "x": 1,
        #         "y": 1
        #         }
        #     ],
        #     "moveBase": {
        #         "x": 1,
        #         "y": 1
        #     }
        # }

    def Participate(self):
        response = requests.put(self.serverURL + "/play/zombidef/participate", headers=self.headers)
        
        # Логирование
        logging.info(f"Participate: {response._content}")
        print(f"Participate: {response._content}")

        return response._content

        # Content type: application/json
        # {
        #     "startsInSec": 300
        # }

    def GetDynamicObjects(self):
        response = requests.get(self.serverURL+ "/play/zombidef/units", headers=self.headers)

        # Логирование
        logging.info(f"GetDynamicObjects: {response._content}")
        print(f"GetDynamicObjects: {response._content}")

        return response._content
    
        # {
        #     "base": [
        #         {
        #         "attack": 10,
        #         "health": 100,
        #         "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
        #         "isHead": true,
        #         "lastAttack": {
        #             "x": 1,
        #             "y": 1
        #         },
        #         "range": 5,
        #         "x": 1,
        #         "y": 1
        #         }
        #     ],
        #     "enemyBlocks": [
        #         {
        #         "attack": 10,
        #         "health": 100,
        #         "isHead": true,
        #         "lastAttack": {
        #             "x": 1,
        #             "y": 1
        #         },
        #         "name": "player-test",
        #         "x": 1,
        #         "y": 1
        #         }
        #     ],
        #     "player": {
        #         "enemyBlockKills": 100,
        #         "gameEndedAt": "2021-10-10T10:00:00Z",
        #         "gold": 100,
        #         "name": "player-test",
        #         "points": 100,
        #         "zombieKills": 100
        #     },
        #     "realmName": "map1",
        #     "turn": 1,
        #     "turnEndsInMs": 1000,
        #     "zombies": [
        #         {
        #         "attack": 10,
        #         "direction": "up",
        #         "health": 100,
        #         "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
        #         "speed": 10,
        #         "type": "normal",
        #         "waitTurns": 1,
        #         "x": 1,
        #         "y": 1
        #         }
        #     ]
        # }

    def GetStaticObjects(self):
        response = requests.get(self.serverURL+ "/play/zombidef/world", headers=self.headers)
        
        # Логирование
        logging.info(f"GetStaticObjects: {response._content}")
        print(f"GetStaticObjects: {response._content}")

        return response
    
        # {
        #     "realmName": "map1",
        #     "zpots": [
        #         {
        #         "x": 1,
        #         "y": 1,
        #         "type": "default"
        #         }
        #     ]
        # }   

    def GameRounds(self):
        response = requests.get(self.serverURL+ "/rounds/zombidef", headers=self.headers)
        
        # Логирование
        logging.info(f"GameRounds: {response._content}")
        print(f"GameRounds: {response._content}")

        return response

        # Content type: application/json
        # {
        #     "gameName": "defense",
        #     "now": "2021-01-01T00:00:00Z",
        #     "rounds": [
        #         {
        #         "duration": 60,
        #         "endAt": "2021-01-01T00:00:00Z",
        #         "name": "Round 1",
        #         "repeat": 1,
        #         "startAt": "2021-01-01T00:00:00Z",
        #         "status": "active"
        #         }
        #     ]
        # }