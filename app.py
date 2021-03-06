from flask import Flask, render_template, jsonify
import json
import recopila
import eliminar_paises

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('template.html')


@app.route('/mi-link/')
def my_link():
    return recopila.recopilacion()


@app.route('/jsonpaises', methods=['GET'])
def leerjson():
    with open('dato_pais.json') as f:
        data = json.load(f)
        return jsonify(data)


@app.route('/eliminar')
def eliminar():
    eliminar_paises.eliminar()
    return render_template('eliminado.html')


if __name__ == '__main__':
    app.run(debug=True)
