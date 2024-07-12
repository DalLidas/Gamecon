import requests

token = "6689b960e0e1b6689b960e0e1e"

mainServerURL = "https://games.datsteam.dev"
testServerURL = "https://games-test.datsteam.dev"

turnTime = 1 # время одного хода

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "ключ": "значение"
}

response = requests.post(testServerURL, headers=headers, json=data)

if response.status_code == 200:
    print("Запрос успешно отправлен")
    print("Ответ сервера:", response.json())
else:
    print("Ошибка при отправке запроса")
    print("Код ошибки:", response.status_code)