import os
import json
import time
import threading
from decouple import config  
from datetime import datetime

from Api import Api
from Model import Model
#from UI import UI

token = config("TOKEN")
mainServerURL = config("MAIN_SERVER_URL")
testServerURL = config("TEST_SERVER_URL")

# Предстоящие раунды
rounds = []

# Всё время должно быть в ms 
startTime = 0
endTime = 0
turnTime = 0

allRequestTime = 0 # ms
allRequestCount = 0 # int

meanRequestLag = 0 # ms
safeOffset = 25 # ms

def lagCheck(func):
    global allRequestTime
    global allRequestCount
    global meanRequestLag

    if allRequestCount < 25:  
        st = time.time() * 1000
        response = func()
        executeTime = st - time.time() * 1000
        print(executeTime)
        allRequestTime += executeTime
        allRequestCount += 1
        meanRequestLag = allRequestTime // allRequestCount
        return response
    else:
        return func()

def main() -> None:
    # Подключение к серверу
    api = Api(mainServerURL, token)
    #ui = UI()
    model = Model()

    try:
        def worker() -> None:
            while not ApplicationStopEvent.is_set():
                
                startsInSec = 0
                repeat = 0

                # # рукопожатие (регистрация на раунд)
                # while 1:
                #     time.time
                #     response = lagCheck(api.Participate)
                #     try:
                #         if response["startsInSec"] is not None:
                #             startsInSec = int(response["startsInSec"])
                #             repeat = int(response["repeat"])
                #             break
                #     except:
                #         time.sleep(2)
                #         continue
                
                # print(f"Ожидание раунда(startsInSec:{startsInSec}, lag:{meanRequestLag} // {safeOffset})")
                # time.sleep(startsInSec - (meanRequestLag-safeOffset)/1000)
                
                # Начало игры
                repeat = 100
                turnIndex = 0 
                while turnIndex <= repeat :
                    print("Начало хода")
                    unitResponse = lagCheck(api.GetUnitsObjects)
                    worldResponse = lagCheck(api.GetWorldObjects)

                    # uiThread = threading.Thread(target=ui.Update(unitResponse, worldResponse))
                    # uiThread.start()
                    #ui.Update(unitResponse, worldResponse)

                    ans = model.Run(unitResponse, worldResponse)
                    
                    # def ModelAnswer():
                    #     global ans
                    #     while not modelStopEvent.is_set():
                            
                            
                    #         # Палка в колесе
                    #         # time.sleep(0.5)
                    #     print("Модель дала ответ")

                    # # Создаем событие для остановки потока
                    # modelStopEvent = threading.Event()

                    # # Создаем и запускаем поток
                    # modelAnswerThread = threading.Thread(target=ModelAnswer)
                    # modelAnswerThread.start()
                    
                    # # Устанавливаем таймер для остановки потока модели
                    # timer = threading.Timer((int(unitResponse["turnEndsInMs"]) - safeOffset)/1000, modelStopEvent.set)
                    # timer.start()

                    # Ждем завершения потока
                    # modelAnswerThread.join()
                    
                    api.Command(ans)
                    print("Конец хода")
                    turnIndex += 1
                

        def control() -> None:
            while 1:
                pass
                # ans = input("Введите: ")
                # print(ans)

                # if ans == "exit":
                #     ApplicationStopEvent.set()
                #     return
        
        # Создаем событие для остановки потока
        ApplicationStopEvent = threading.Event()

        # Создаем и запускаем поток
        workerThread = threading.Thread(target=worker)
        controlThread = threading.Thread(target=control)
        workerThread.start()
        controlThread.start()

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