import os
import time
import threading
from decouple import config  

from Api import Api
from Model import Model

token = config("TOKEN")
mainServerURL = config("MAIN_SERVER_URL")
testServerURL = config("TEST_SERVER_URL")

# Всё время должно быть в ms 
startTime = 0
endTime = 0
turnTime = 0

meanRequestLag = 0
safeOffset = 10


def main() -> None:
    try:
        def worker() -> None:
            while not workerStopEvent.is_set():
                api = Api(testServerURL, token)
                #response = api.GameRounds()
                response = api.Participate()
                time.sleep(1)

                # while 1:d
                #     response = api.Participate()
                #     time.sleep(1)


                #model.
                # def ModelAnswer():
                #     while not modelStopEvent.is_set():
                #         #model.
                #         time.sleep(0.5)
                #     print("Модель дала ответ")

                # # Создаем событие для остановки потока
                # modelStopEvent = threading.Event()

                # # Создаем и запускаем поток
                # modelAnswerThread = threading.Thread(target=ModelAnswer)
                # modelAnswerThread.start()

                # # Устанавливаем таймер на 5 секунд для остановки потока
                # timer = threading.Timer(0.6, modelStopEvent.set)
                # timer.start()

                # # Ждем завершения потока
                # modelAnswerThread.join()
                # print("Программа завершена")

        def control():
            while 1:
                ans = input("Введите: ")
                print(ans)

                if ans == "exit":
                    workerStopEvent.set()
                    return


         # Создаем событие для остановки потока
        workerStopEvent = threading.Event()

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