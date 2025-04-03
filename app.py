from flask import Flask, jsonify, render_template, request
import requests
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('index.html')

@app.route('/cve_results', methods=['POST'])
def getVulnerabilityForCVE():
    vulnerability_id = request.form.get('vendor')
    
    if not vulnerability_id:
        return "No se proporcionó el parámetro 'vendor'.", 400
    
    # URL para la API
    url = f"https://cve.circl.lu/api/vulnerability/{vulnerability_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        vulnerabilities = response.json()  # Esto devuelve la vulnerabilidad detallada
        return render_template('cve_results.html', vulnerability_id=vulnerability_id, vulnerabilities=vulnerabilities)
    else:
        return jsonify({"error": "No se pudo obtener la información."}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
