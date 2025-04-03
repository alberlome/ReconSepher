from flask import Flask, jsonify, render_template, request
import requests
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('index.html')

@app.route('/cve_results', methods=['POST'])
def getCVEforVendor():
    vendor = request.form.get('vendor')
    
    if not vendor:
        return "No se proporcionó el parámetro 'vendor'.", 400
    
    # URL para la API
    url = "https://cve.circl.lu/api/browse/"
    params = {
        'vendor': vendor,
        'page': 1  # Puedes agregar más parámetros aquí si lo deseas
    }

    # Realizamos la solicitud GET a la API
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Mostrar la respuesta completa en consola para depuración
        print(response.json())  # Esto imprimirá el JSON completo
        cves = response.json()  # Esto devuelve la lista completa
        return render_template('cve_results.html', vendor=vendor, cves=cves)
    else:
        return jsonify({"error": "No se pudo obtener la información."}), 500

if __name__ == '__main__':
    app.run(debug=True)
