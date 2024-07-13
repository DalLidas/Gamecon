import requests
import json
import os
import time
from decouple import config  

from Api import Api
from Model import Model

token = config("TOKEN")
mainServerURL = config("MAIN_SERVER_URL")
testServerURL = config("TEST_SERVER_URL")

turnTime = 1 # время одного хода

def main() -> None:
    try:
        api = Api(testServerURL, token)

        # while 1:
        #     response = api.Participate()
        #     time.sleep(1)
        
        response = api.Participate()

        print(type(response))
    except Exception as e:
        print(e)
        print("Ёпт, да как так-то. Обещали же что не эбонёт, разрабы паханы полные")

    '''
    TODO:
    !общая организация цикла работы программы:
        1. Нужно вопервых GameRounds() для понимания стадии, потом начать стучатся до серва Participate()
        2. Выполнить вызов GetDynamicObjects() и GetStaticObjects() для заполнения модели 
        3. Ожидания ответа от модели
        4. Выполнения Command()
        5. Конец раунда

    Какие тонкости?:
        1. Долгий ответ от модели. Может быть долгий ответ (Нельзя ассинхронно вызывать модель,
           а иначе возможна стрельба в призраки, но желательно асинхронное выполнения алгоритмов модели)
        2. Задержки при отправки запросов. Нужно считать время отправки запроса и делать на это поправку
        3. Делать проверку на отправленный запрос. Вдруг он не дошёл
        4. Что делать если не готов ответ от модели? Браться считать следующий раунд? 
    '''

if __name__ == "__main__":
    main()