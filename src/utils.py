import requests
import json
import os
import uuid

def get_uniques(elements):

    return_list = []

    for element in elements:

        if element not in return_list:

            return_list.append(element)

    return return_list


def get_relation_types():

    url = 'https://api.conceptnet.io/c/en/word?limit=10000'

    response = requests.get(url)
    
    if response.status_code == 200:

        response = json.loads(response.text)


    content = response['edges']
    types = []

    for edge in content:

        types.append(edge['rel']['@id'])

    types = get_uniques(types)

    return types


def get_url(query,lang):

    url = f'https://api.conceptnet.io/uri?language={lang}&text={query}'
    response = requests.get(url)
    
    if response.status_code == 200:

        response = response.json()


    return response['@id']


def get_datasets(url, amount = 1000):

    new_url = url + f'?limit={amount}'
    
    response = requests.get(new_url)
    

    if response.status_code == 200:

        response = response.json()

    content = response['edges']

    datasets = []

    for edge in content:

        datasets.append(str(edge['dataset']))

    result = []

    for dataset in datasets:

        if dataset not in result:

            result.append(dataset)


    return result


def create_file(content):
        
    data = json.dumps(content, indent = 4)

    dir_path = str(os.getcwd()) + '/files/'
    file_id = str(uuid.uuid1())
    file_name = f'{file_id}.json'

    file_path = os.path.join(dir_path, file_name)
    
    with open(file_path, 'w') as f:

        f.write(data)

    return file_path
