import requests
import json

def make_request(query, lang, amount = 1000):

    url = f'https://api.conceptnet.io/c/{lang}/{query}?limit={amount}'

    response = requests.get(url)
    
    if response.status_code == 200:

        response = response.content
    
    response = json.loads(response)

    return response


def get_relations(edges):

    result = []

    for edge in edges:
        
        try:
            start = edge['start']['label']
            end = edge['end']['label']
            relation = edge['rel']['label']
            weight = round(float(edge['weight']), 2)
            language = edge['start']['language'] + ' --> ' + edge['end']['language'] 
            node = dict()

            node['Start'] = start
            node['End'] = end
            node['Relation'] = relation
            node['Language'] = language
            node['Weight'] = weight
            
            base_url = 'https://api.conceptnet.io'

            start_url = base_url + str(edge['start']['@id'])
            end_url = base_url + str(edge['end']['@id'])

            urls = [start_url,end_url]

            node['URLs'] = urls
            node['Usage'] = edge['surfaceText']

            result.append(node)
        except:

            pass
        
    return result



def response(query, lang, amount = 1000):

    content = make_request(query, lang, amount)
    content = get_relations(content['edges'])
    
    return content
