import requests 
import os

import logging

class Api:
    def __init__(self, serverURL, token, *, debugMod = True):
        self.serverURL = serverURL
        self.token = token
        self.debugMod = debugMod

        # Генерация имени лога
        index = 0
        logFileName = "app_requests.log"
        logDir = "log"
        while 1:
            if not os.path.isdir(logDir): os.makedirs(logDir)

            if os.path.exists(f"log\\{index}.{logFileName}"): index += 1
            else:
                logFileName = f"log\\{index}.{logFileName}"
                break

        # Настройка логгера
        logging.basicConfig(filename=logFileName, 
                            level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')


        # Хедер
        self.headers = {
            "X-Auth-Token": f"{token}",
            "Content-Type": "application/json"
        }

    def Command(self, attacked, build, moveBase):
        try:
            response = requests.post(self.serverURL + "/play/zombidef/command", 
                                    headers=self.headers, 
                                    json={"attack": attacked, "build": build, "moveBase": moveBase})

            # Логирование
            if self.debugMod: 
                logging.info(f"Command - {response._content}")
                #print(f"Command - {response._content}")

            return response.json()
        except Exception as e:
            print(e)

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
        try:
            response = requests.put(self.serverURL + "/play/zombidef/participate", headers=self.headers)
            
            # Логирование
            if self.debugMod: 
                logging.info(f"Participate - {response._content}")
                #print(f"Participate - {response._content}")

            return response.json()
        except Exception as e:
            print(e)

        # Content type: application/json
        # {
        #     "startsInSec": 300
        # }

    def GetUnitsObjects(self):
        try:
            response = requests.get(self.serverURL+ "/play/zombidef/units", headers=self.headers)

            # Логирование
            if self.debugMod: 
                logging.info(f"GetUnitsObjects - {response._content}")
                #print(f"GetUnitsObjects - {response._content}")

            return response.json()
        except Exception as e:
            print(e)
    
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

    def GetWorldObjects(self):
        try:
            response = requests.get(self.serverURL+ "/play/zombidef/world", headers=self.headers)
            
            # Логирование
            if self.debugMod: 
                logging.info(f"GetWorldObjects - {response._content}")
                #print(f"GetWorldObjects - {response._content}")

            return response.json()
        except Exception as e:
            print(e)

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
        try:
            response = requests.get(self.serverURL+ "/rounds/zombidef", headers=self.headers)
            
            # Логирование
            if self.debugMod: 
                logging.info(f"GameRounds - {response._content}")
                #print(f"GameRounds - {response._content}")

            return response.json()
        except Exception as e:
            print(e)

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