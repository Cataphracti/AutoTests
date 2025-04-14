import requests
import json




def mp_auth():
    body = json.dumps({
    "client_id": "3_3vdu2rvr7t4wws844gkcs8kwow4w8gc8gkkgswg84c84wwsssc",
    "client_secret": "14f0b16kgoyoc8ckg0wokgwc0004848w4kkg084co0w0g448w0",
    "username": "zlnslnk1999@gmail.com",
    "password": "1763914Ellina",
    "grant_type": "https://api.smartseeds.ru/grants/carrier-pin-code",
    "scope": "android"
    })
    headers = {
        'User-Agent':'Smartseeds.Driver (Android 14; samsung A34 polzovatelya Alen; 2.0.12)',
        'Accept':'*/*',
        'Content-Type':'application/json; charset=utf-8'
    }
    authmp = requests.post('https://api.smartseeds.ru/oauth/v2/token', data=body, headers=headers)#.json()
    print("Статус код получения токена:", authmp.status_code)  # Выводим статус до проверки

    if authmp.status_code != 200:
        print("Ошибка! Ответ сервера:", authmp.text)  # Выводим сырой ответ (не JSON)

    assert authmp.status_code == 200, f"Ожидался статус 200, но получен {authmp.status_code}"
    token = authmp.json()["access_token"]  # Отрабатывает только если статус 200
    return f"Bearer {token}"


def get_mp_vehicles_list():
    token = mp_auth()
    headers = {
        'User-Agent': 'Smartseeds.Driver (Android 14; samsung A34 polzovatelya Alen; 2.0.12)',
        'Accept': '*/*',
        'Authorization': token  # Используем токен из mp_auth()
    }
    vehicles_list = requests.get(
        'https://api.smartseeds.ru/v1.0/vehicles?page=1&per-page=10000&order-by=id%7CASC',
        headers=headers
    )

    print("Статус код списка ТС:", vehicles_list.status_code)  # Для отладки

    if vehicles_list.status_code != 200:
        print("Ошибка запроса списка ТС! Ответ сервера:", vehicles_list.text)
        exit(1)

    assert vehicles_list.status_code == 200
    print(vehicles_list.json())




#mp_auth()
get_mp_vehicles_list()