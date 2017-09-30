from flask import Flask, request, json

app = Flask(__name__)

@app.route('/api/analysis', methods=['GET', 'POST'])
def analysis():
    request_json = request.get_json()

    if request_json is not None:
        text = request_json.get('text')
        lang = request_json.get('lang')

        ## TODO: do some fancy stuff...

        return json.jsonify({
            'similar_words': None,
            'text' : text
            })

    return json.jsonify({'error': 'please provide a tweet as json'})
