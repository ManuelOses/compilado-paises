from flask import Flask, jsonify
import recopila
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return recopila.recopilacion()


@app.route('/jsonpaises', methods=['GET'])
def leerjson():
    with open('templates/dato_pais.json') as f:
        data = json.load(f)
        return jsonify(data)


if __name__ == '__main__':
    app.run()
