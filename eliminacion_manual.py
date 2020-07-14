import json


def eliminar_datos():
    with open('dato_pais.json') as json_data:
        data = json.load(json_data)
        for a in data['paises'][:]:
            if a['nombrePais'] != '':  # Se elimina paises registrados anteriormente
                data['paises'].remove(a)
                with open('dato_pais.json', 'w') as f:
                    json.dump(data, f)
    return
