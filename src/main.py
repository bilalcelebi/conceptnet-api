from flask import Flask, jsonify, request, send_file
from getres import response
import get_related
from utils import get_relation_types, get_url, get_datasets, create_file
from get_rels import get_relation_data
from example import example

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/word/<string:lang>/<string:name>/<int:amount>/')
def hello_world(name,lang,amount):
    
    download = request.args.get('download')
    result = response(name,lang,amount)
  
    if download == 'False':

        return jsonify(result)

    else:

        file_path = create_file(result)
        
        return send_file(file_path, as_attachment = True)


@app.route('/related/<string:lang>/<string:word>/<int:amount>/')
def related(word,lang,amount):
    
    download = request.args.get('download')
    result = get_related.response(str(word), str(lang), int(amount))

    if download == 'False':
        
        return jsonify(result)

    else:

        file_path = create_file(result)

        return send_file(file_path, as_attachment = True)


@app.route('/get_relations')
def relation_listing():

    result = get_relation_types()
    
    return jsonify(result)


@app.route('/get_url')
def generate_url():

    word = request.args.get('word')
    lang = request.args.get('lang')

    result = get_url(str(word), str(lang))

    return jsonify(result)


@app.route('/get_relation')
def relation_data():

    download = request.args.get('download')
    relation = request.args.get('relation')
    amount = request.args.get('amount')

    result = get_relation_data(str(relation), int(amount))
    
    if download == 'False':
        return jsonify(result)
    else:
        file_path = create_file(result)
        return send_file(file_path, as_attachment = True)

@app.route('/example')
def get_example():
    
    download = request.args.get('download')
    result = example()
    file_path = create_file(result)
   
    if download == 'True':

        return send_file(file_path, as_attachment = True)

    else:

        return jsonify(result)


@app.route('/get_datasets')
def datasets():

    lang = request.args.get('lang')
    word = request.args.get('word')
    
    url = f'https://api.conceptnet.io/c/{lang}/{word}'

    result = get_datasets(url,1000)

    return jsonify(result)

