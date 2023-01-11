import requests

def example():

    url = f'https://api.conceptnet.io/c/en/example?limit=1000'

    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
    
    content = response['edges']

    result = []
    
    for edge in content:
        
        try:
            
            start = edge['start']['label']
            end = edge['end']['label']
            language = edge['start']['language'] + ' --> ' + edge['end']['language']
            weight = round(float(edge['weight']), 2)
            dataset = edge['dataset']
            relation = edge['rel']['label']
        
            base_url = 'https://api.conceptnet.io'

            start_url = base_url + edge['start']['@id']
            end_url = base_url + edge['end']['@id']

            urls = [start_url,end_url]
            surface_text = str(edge['surfaceText'])
            node = dict()

            node['Start'] = start
            node['End'] = end
            node['Language'] = language
            node['Relation'] = relation
            node['Weight'] = weight
            node['Dataset'] = dataset
            node['URLs'] = urls
            node['Usage'] = surface_text

            result.append(node)
        
        except:

            pass

    return result
