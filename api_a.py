# api_a.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_B_URL = "http://localhost:5001/weather"

@app.route('/recommendation/<city>', methods=['GET'])
def get_recommendation(city):
    try:
        response = requests.get(f"{API_B_URL}/{city}")
        if response.status_code != 200:
            return jsonify({"error": "Erro ao obter dados da cidade"}), response.status_code

        data = response.json()
        temp = data.get("temp")

        if temp is None:
            return jsonify({"error": "Temperatura nao disponivel"}), 500

        # Lógica de recomendação
        if temp > 30:
            recommendation = "Esta quente! Beba bastante água e use protetor solar."
        elif 15 < temp <= 30:
            recommendation = "O clima esta agradavel. Aproveite o dia!"
        else:
            recommendation = "Esta frio! Não esqueça de usar um casaco."

        return jsonify({
            "city": data["city"],
            "temp": temp,
            "unit": data["unit"],
            "recommendation": recommendation
        })

    except requests.RequestException as e:
        return jsonify({"error": "Erro ao conectar a API de clima"}), 500

if __name__ == '__main__':
    app.run(port=5000)
