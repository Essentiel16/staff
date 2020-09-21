import requests

URL = "http://127.0.0.1:8000"


def get_token():
    url = f"{URL}/api/auth/"
    response = requests.post(url, data={'username': 'Leventis',
                                        'password': 'xyquabrt'})
    return response.json()


def get_data():
    url = f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    emp_data = response.json()
    for e in emp_data:
        print(e)


get_data()


def delete_data(firstName):
    url = f"{URL}/api/users_list/{firstName}/"
    header = {'Authentication': f'Token {get_token()}'}
    response = requests.delete(url, headers=header)
    print(response.status_code)


for e in range(1000):
    if e > 5:
        delete_data(e)
