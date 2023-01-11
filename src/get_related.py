import requests

def make_request(word, lang, limit):

    url = f'https://api.conceptnet.io/related/c/{lang}/{word}?limit={limit}'
    response = requests.get(url)

    if response.status_code == 200:

        response = response.json()

    return response['related']



def response(word, lang, limit):

    content = make_request(word,lang,limit)

    response = []

    for edge in content:
        
        pairs = str(edge['@id']).split('/')

        word = pairs[3]
        lang = pairs[2]
        weight = round(float(edge['weight']), 2)
        
        node = dict()

        node['Word'] = word
        node['Language'] = lang
        node['weight'] = weight

        response.append(node)

    return response
