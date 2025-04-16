# api_b.py
from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de dados de temperatura por cidade
weather_data = {
    "SaoPaulo": 25,
    "RioDeJaneiro": 32,
    "Curitiba": 14,
    "Salvador": 29,
    "PortoAlegre": 18
}

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    city_key = city.replace(" ", "")
    temp = weather_data.get(city_key)

    if temp is None:
        return jsonify({"error": "Cidade nao encontrada"}), 404

    return jsonify({
        "city": city_key,
        "temp": temp,
        "unit": "Celsius"
    })

if __name__ == '__main__':
    app.run(port=5001)
