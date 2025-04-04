from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('index.html')

def fetchCveData(cve):
    url = f"https://cve.circl.lu/api/vulnerability/{cve}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json() 
                if data is not None:
                    return data.get("containers", {})
                else:
                    return {}
            except ValueError:
                return {}
        else:
            return {}
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return {}

@app.route('/cve_results', methods=['POST'])
def getVulnerabilityForCVE():
    cve = request.form.get('cve')
    if not cve:
        return jsonify({"error": "No se proporcionó el parámetro 'cve'."}), 400
    containers = fetchCveData(cve)
    if not containers:
        return render_template('cve_results.html', cve=cve, containers=None)
    return render_template('cve_results.html', cve=cve, containers=containers)

if __name__ == '__main__':
    app.run(debug=True)
