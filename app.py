from flask import Flask, jsonify, render_template
import recopila
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('template.html')


@app.route('/mi-link/')
def my_link():
    return recopila.recopilacion()


@app.route('/jsonpaises', methods=['GET'])
def leerjson():
    with open('dato_pais.json') as f:
        data = json.load(f)
        return jsonify(data)


if __name__ == '__main__':
    app.run()
