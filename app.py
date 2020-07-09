from flask import Flask , jsonify,request
import recopila
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return recopila()


@app.route('/jsonpaises', methods=['GET'])
def recopilar_pais():
    with open('templates/dato_pais.json') as f:
        data = json.load(f)
        return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')