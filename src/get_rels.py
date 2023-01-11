import requests


def make_request(relation, offset):

    url = f'https://api.conceptnet.io/r/{relation}?offset={offset}&limit=1000'
    
    print(url)
    response = requests.get(url)

    if response.status_code == 200:

        response = response.json()

    return response['edges']



def prepare_list(edges):

    result = []

    for edge in edges:
        
        try:

            start = edge['start']['label']
            end = edge['end']['label']
            rel = edge['rel']['label']
            dataset = edge['dataset']
            weight = round(float(edge['weight']), 2)
            lang = str(edge['start']['language']) + ' --> ' + str(edge['end']['language'])

            base_url = 'https://api.conceptnet.io'

            start_url = base_url + edge['start']['@id']
            end_url = base_url + edge['end']['@id']
        
            urls = [start_url,end_url]

            node = dict()

            node['Start'] = start
            node['End'] = end
            node['Languages'] = lang
            node['Relation'] = rel
            node['weight'] = weight
            node['Dataset'] = base_url + dataset
            node['URLs'] = urls

            result.append(node)

        except:

            pass

    return result


def get_relation_data(relation, amount):

    response = []

    offset = 0

    for i in range(amount):

        content = make_request(relation, offset)
        conntent = prepare_list(content)

        for edge in content:

            response.append(edge)

            
        offset += 1000

    return prepare_list(response)
