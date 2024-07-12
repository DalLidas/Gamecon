import requests
import json

import Api

token = "6689b960e0e1b6689b960e0e1e"

mainServerURL = "https://games.datsteam.dev"
testServerURL = "https://games-test.datsteam.dev"

turnTime = 1 # время одного хода

def main():
    api = Api(testServerURL, token)

    api.Participate()

if __name__ == "__main__":
    main()