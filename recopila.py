from selenium import webdriver
import json
import eliminar_paises
import os


def recopilacion():
    # opcion_chrome = webdriver.ChromeOptions()
    # opcion_chrome.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # opcion_chrome.add_argument("--headless")
    # opcion_chrome.add_argument("--disable-dev-shm-usage")
    # opcion_chrome.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=opcion_chrome)
    driver = webdriver.Chrome(executable_path=r"Drivers\chromedriver.exe")
    driver.get('http://example.webscraping.com/places/default/index/')

    # Verificador de datos existentes en dato_pais.json
    eliminar_paises.eliminar()

    revisar_pagina = True
    while revisar_pagina:
        paises = driver.find_elements_by_tag_name('td')
        cantidad_pais = len(paises)
        pagination = driver.find_element_by_id('pagination')
        siguiente_pagina = pagination.find_elements_by_tag_name('a')
        with open('dato_pais.json') as f:
            data = json.load(f)
        for i in range(len(siguiente_pagina)):
            cant_tag_a = len(siguiente_pagina)
            if cant_tag_a == 1:
                if siguiente_pagina[i].text == 'Next >':
                    for e in range(cantidad_pais):
                        revisar_pagina = True
                        data['paises'].append({'nombrePais': paises[e].text})
                    with open('dato_pais.json', 'w') as f:
                        json.dump(data, f)
                    siguiente_pagina[i].click()

                elif siguiente_pagina[i].text == '< Previous':
                    for e in range(cantidad_pais):
                        revisar_pagina = False
                        data['paises'].append({'nombrePais': paises[e].text})
                    with open('dato_pais.json', 'w') as f:
                        json.dump(data, f)
                else:
                    revisar_pagina = False

            elif cant_tag_a == 2:
                if siguiente_pagina[i].text == 'Next >':
                    for e in range(cantidad_pais):
                        revisar_pagina = True
                        data['paises'].append({'nombrePais': paises[e].text})
                    with open('dato_pais.json', 'w') as f:
                        json.dump(data, f)
                    siguiente_pagina[i].click()
                elif siguiente_pagina[i].text == '< Previous':
                    revisar_pagina = True

                else:
                    revisar_pagina = False
                    break
    # Inicio de Relleno de datos de Nueva Zelanda
    driver.get('http://example.webscraping.com/places/default/view/New-Zealand-159')
    with open('dato_pais.json', 'r') as f:
        data = json.load(f)
    fila = driver.find_elements_by_tag_name('tr')
    seguimiento_nz_json = True
    while seguimiento_nz_json:
        for elemento in data['paises']:
            if elemento['nombrePais'] == 'New Zealand':
                for a in range(1, 4):
                    columna = fila[a].find_elements_by_tag_name('td')
                    tipo = columna[0].text
                    valor = columna[1].text
                    if valor == "":
                        valor = "NULL"
                    elemento[tipo] = valor
                for b in range(5, len(fila)):
                    columna = fila[b].find_elements_by_tag_name('td')
                    tipo = columna[0].text
                    valor = columna[1].text
                    if valor == "":
                        valor = "NULL"
                    elemento[tipo] = valor
                seguimiento_nz_json = False
                with open('dato_pais.json', 'w') as e:
                    json.dump(data, e)
            else:
                seguimiento_nz_json = True
    return