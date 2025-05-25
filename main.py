import flask
import requests
from googlesearch import search

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'api is running'

@app.route('/dork', methods=['GET'])
def dork():
    dorks = flask.request.args.get('dorks')
    hasil = flask.request.args.get('hasil', default='5')
    nums = int(hasil)
    result = []
    for x in search(dorks, num_results=nums):
        result.append(x)
    return flask.jsonify({'result':result})
if __name__=='__main__':
    app.run(debug=True)