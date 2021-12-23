import requests
import json

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ' '
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(name):
    new_folder = requests.put(f'{URL}?path={name}', headers=headers)
    return new_folder.status_code


def get_status_folder(name):
    params = {'path': name}
    result = requests.get(URL, headers=headers, params=params)
    if result.status_code == 200:
        res_dict = json.loads(result.text)
        print(result)
        return res_dict.get('type')


if __name__ == '__main__':
    create_folder('unit_test')
    get_status_folder('unit_test')
