import requests # type: ignore
import json

class Api:
    def __init__(self, serverURL, token):
        self.serverURL = serverURL
        self.token = token

        self.headers = {
            # "API Key": "ApiKeyAuth",
            # "Header parameter name": f"{token}"

            "X-Auth-Token": f"{token}",
            "Content-Type": "application/json"
        }

    def CommandAttack(self, attacked, build, moveBase):
        data = json.JSONEncoder({"attack": attacked, "build": build, "moveBase": moveBase})
        response = requests.post(self.serverURL+ "/lay/zombidef/command", headers=self.headers, json=data)
        print(response)
        return json.JSONDecoder(response)

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
        print(self.serverURL + "/play/zombidef/participate", self.headers)
        print(response.headers, "||", response._content, "||", response._content.decode('utf-8'))
        return response

        # Content type: application/json
        # {
        #     "startsInSec": 300
        # }

    def GetDynamicObjects(self):
        response = requests.get(self.serverURL + "/play/zombidef/units", headers=self.headers)
        print(response)
        return json.JSONDecoder(response)
    
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
        response = requests.get(self.serverURL+ "/play/zombidef/participate", headers=self.headers)
        print(response)
        return json.JSONDecoder(response)
    
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
        print(response)
        return json.JSONDecoder(response)

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